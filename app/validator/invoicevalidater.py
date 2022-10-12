from array import array
from datetime import datetime
from flask import jsonify, request, session
class Invoicevalidator(object):
    def rule(self):
        rule = {
        "invoice_terms": "required|string",
        "invoice_date":  self.date_time_validator, 
        "due_date": self.date_time_validator,
        "sub_total": self.func_float,
        "tax_total_amount":self.func_float,
        "shipping_charges":self.func_float,
        "invoice_number":"required|string",
        "total_invoice_amount":self.func_float,
        "customer_note":"required|string",
        "user_id":"required|integer",
        "contact_id":"required|integer",
        "salesperson_id":"required|integer",
        "invoiceItems": self.func_invoiceItems}
        return rule

        
    def func_invoiceItems(self, items):

        ret = True
        if isinstance(items, list):
            result = {}
            result["invoiceItems"] = {}
            l = 0
            for item in items:
                result["invoiceItems"][l] = {}
                if 'id' in item:
                    if not isinstance(item['id'], int): 
                        result["invoiceItems"][l]["id"]  = "Id must be integer"
                        ret = False
                else:
                        result["invoiceItems"][l]["id"]  = "Id field required"
                        ret = False

                if 'user_id' in item:
                    if not isinstance(item['user_id'], int): 
                        result["invoiceItems"][l]["user_id"]  = "User Id must be integer"
                        ret = False 

                if 'name' in item:
                    if not isinstance(item['name'], str): 
                        result["invoiceItems"][l]["name"]  = "Name must be String"
                        ret = False 

                if 'description' in item:
                    if not isinstance(item['description'], str): 
                        result["invoiceItems"][l]["description"]  = "Description must be string"
                        ret = False 
                if 'upc' in item:
                    if not isinstance(item['upc'], str): 
                        result["invoiceItems"][l]["upc"]  = "UPC must be string"
                        ret = False 

                if 'sku' in item:
                    if not isinstance(item['sku'], str): 
                        result["invoiceItems"][l]["sku"]  = "SKU must be string"
                        ret = False 
                
                if 'price' in item:
                    if not isinstance(item['price'], int) and not isinstance(item['price'], float): 
                        result["invoiceItems"][l]["price"]  = "Price must be float"
                        ret = False 
                
                if 'quantity' in item:
                    if not isinstance(item['quantity'], int): 
                        result["invoiceItems"][l]["quantity"]  = "Quantity must be integer"
                        ret = False 
                
                if 'total_amount' in item:
                    if not isinstance(item['total_amount'], float) and not isinstance(item['price'], int): 
                        result["invoiceItems"][l]["total_amount"]  = "Total Amount must be float"
                        ret = False     
                
                if 'created_at' in item and item['created_at'] !=None:
                        rets = self.date_time_validator_no_zone(item['created_at'])
                        if rets == False:
                            ret = False
                            result["invoiceItems"][l]["created_at"]  = "Created At invalide date formate"
                
                if 'updated_at' in item and item['updated_at'] !=None:
                        rets = self.date_time_validator_no_zone(item['updated_at']) 
                        if rets == False:
                            ret = False
                            result["invoiceItems"][l]["updated_at"]  = "Updated At invalide date formate"
                if len(result["invoiceItems"][l]) == 0:
                    del result["invoiceItems"][l]
                l = l + 1

                        

            if result:
                session["validation"] = result
             
            return ret
        else:
            return False

    def func_bool(self,x):
        if x == True:
            return True
        elif x == False:
            return True
        else:
            return False
    
    def func_float(self,x):
        if isinstance(x, float):
            return True
        else:
            if isinstance(x, int):
                return True
            else:
                return False

            

    def date_time_validator(self, time):
        timeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
        try:
            validtime = datetime.strptime(time, timeformat)
            return True
        except ValueError:
            return False
 
    def date_time_validator_no_zone(self, time):
        timeformat = '%Y-%m-%d %H:%M:%S'
        try:
            validtime = datetime.strptime(time, timeformat)
            return True
        except ValueError:
            return False
 