import imp
import json
from sqlalchemy import null, true
from app.models.invoices import InvoicesModel
from app.models.productitems import ProductitemsModel
from app.msmodel.Invoicemodel import Invoicemodel, Invoiceitemsmodel
from app.schemas.invoiceitems import InvoiceitemsSchema
from app.schemas.invoices import InvoicesSchema 

from datetime import datetime,timedelta,date
from app.db import db 
import os,sys

from app.schemas.productitems import ProductitemsSchema


invoice_schema = InvoicesSchema()
invoice_item_schema = InvoiceitemsSchema()
product_item = ProductitemsModel
invoice_model = InvoicesModel
product_item_schema = ProductitemsSchema()


class InvoiceService(object):
 
    def create(self, invoice:Invoicemodel):
        due_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if invoice.invoice_terms == 'due_on_receipt':
                timeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
                due_date = datetime.strptime(invoice.invoice_date, timeformat)
                due_date = due_date.strftime( '%Y-%m-%dT%H:%M:%S')
        
        elif invoice.invoice_terms == 'custom_date':
            timeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
            due_date = datetime.strptime(invoice.due_date, timeformat)
            due_date = due_date.strftime( '%Y-%m-%dT%H:%M:%S')
        else:
            if "net_" in invoice.invoice_terms:
                arr = invoice.invoice_terms.split("net_")
                d = int('+'+arr[1])
                due_date = datetime.strptime( invoice.invoice_date, timeformat)
                
                due_date = due_date + timedelta(days=d)
                due_date = due_date.strftime('%Y-%m-%dT%H:%M:%S')
        
         
        data_invoice = json.loads(json.dumps(invoice.__dict__))
        timeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
        inv_date = datetime.strptime(invoice.invoice_date, timeformat)
        data_invoice['invoice_date'] = inv_date.strftime('%Y-%m-%dT%H:%M:%S')
        data_invoice['due_date'] = due_date
        if 'status' not in data_invoice:
            data_invoice['status'] = 'draft'
        today = date.today()
        d1 = today.strftime('%Y-%m-%dT%H:%M:%S')
        data_invoice['updated_at'] = d1
        del data_invoice['invoiceItems']
        
        inv = 1 
        sub_total = 0
        
    
        save_invoice = invoice_schema.load(data_invoice, session=db.session)
        save_invoice.save_to_db()
        
        #invoice_model.delete_from_db(save_invoice.id)
        # try: 
        for item in invoice.invoiceItems:
            if 'item' in item:
                item_id = item['item']['id'] 
            else:
                item_id = item['id']
            
            item_new = {}
                
            item_new['item']= {"id":item_id} 
            item_new['invoice']= {"id":save_invoice.id} 
            item_new['quantity'] = int(item['quantity'])
            item_new['total_amount'] = round(int(item['quantity']) * round(item['price'], 2),2)
            item_new['price'] = round(item['price'], 2)
            item_new['created_at'] = d1
            save_invoice_item = invoice_item_schema.load(item_new, session=db.session)
            save_invoice_item.save_to_db()
            sub_total = sub_total + item_new['total_amount']
            inv = inv + 1
            
            save_invoice.sub_total = round(sub_total,2)
            total_invoice_amount = sub_total + float(data_invoice['tax_total_amount']) +  float(data_invoice['shipping_charges'])
            save_invoice.total_invoice_amount = round(total_invoice_amount+22, 2)
            
            save_invoice.save_to_db()
        
        return save_invoice
    
    def update(self, invoice:Invoicemodel, id:int):
        print(invoice)
        due_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if invoice.invoice_terms == 'due_on_receipt':
                timeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
                due_date = datetime.strptime(invoice.invoice_date, timeformat)
                due_date = due_date.strftime( '%Y-%m-%dT%H:%M:%S')
        
        elif invoice.invoice_terms == 'custom_date':
            timeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
            due_date = datetime.strptime(invoice.due_date, timeformat)
            due_date = due_date.strftime( '%Y-%m-%dT%H:%M:%S')
        else:
            if "net_" in invoice.invoice_terms:
                arr = invoice.invoice_terms.split("net_")
                d = int('+'+arr[1])
                due_date = datetime.strptime( invoice.invoice_date, timeformat)
                
                due_date = due_date + timedelta(days=d)
                due_date = due_date.strftime('%Y-%m-%dT%H:%M:%S')
        
        invoice_data = InvoicesModel.find_by_id(id)
         
        data_invoice = json.loads(json.dumps(invoice.__dict__))
        timeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
        inv_date = datetime.strptime(invoice.invoice_date, timeformat)
        data_invoice['invoice_date'] = inv_date.strftime('%Y-%m-%dT%H:%M:%S')
        data_invoice['due_date'] = due_date
        if 'status' not in data_invoice:
            data_invoice['status'] = 'draft'
        today = date.today()
        d1 = today.strftime('%Y-%m-%dT%H:%M:%S')
        data_invoice['updated_at'] = d1
        del data_invoice['invoiceItems']
        
        inv = 1 
        sub_total = 0
        

        save_invoice = invoice_schema.load(data_invoice, session=db.session)
        invoice_data.user_id = save_invoice.user_id
        invoice_data.contact_id = save_invoice.contact_id
        invoice_data.salesperson_id = save_invoice.salesperson_id
        invoice_data.invoice_number = save_invoice.invoice_number
        invoice_data.invoice_date = save_invoice.invoice_date
        invoice_data.due_date = save_invoice.due_date
        invoice_data.tax_total_amount = save_invoice.tax_total_amount
        invoice_data.shipping_charges = save_invoice.shipping_charges
        invoice_data.sub_total = save_invoice.sub_total
        invoice_data.total_invoice_amount = save_invoice.total_invoice_amount
        invoice_data.invoice_terms = save_invoice.invoice_terms
        invoice_data.customer_note = save_invoice.customer_note
        invoice_data.status = save_invoice.status
        invoice_data.updated_at = save_invoice.updated_at

        invoice_data.save_to_db()
        
        #invoice_model.delete_from_db(save_invoice.id)
        # try: 
        for item in invoice.invoiceItems:
            if 'item' in item:
                item_id = item['item']['id'] 
            else:
                item_id = item['id']
            
            item_new = {}
                
            item_new['item']= {"id":item_id} 
            item_new['invoice']= {"id":save_invoice.id} 
            item_new['quantity'] = int(item['quantity'])
            item_new['total_amount'] = round(int(item['quantity']) * round(item['price'], 2),2)
            item_new['price'] = round(item['price'], 2)
            item_new['created_at'] = d1
            save_invoice_item = invoice_item_schema.load(item_new, session=db.session)
            save_invoice_item.save_to_db()
            sub_total = sub_total + item_new['total_amount']
            inv = inv + 1
            
            invoice_data.sub_total = round(sub_total,2)
            total_invoice_amount = sub_total + float(data_invoice['tax_total_amount']) +  float(data_invoice['shipping_charges'])
            invoice_data.total_invoice_amount = round(total_invoice_amount+22, 2)
            
            invoice_data.save_to_db()
        
        return invoice_data
 

 




