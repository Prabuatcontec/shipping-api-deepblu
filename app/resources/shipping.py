import imp
from app.helper.shippingspagination import InvoicesPaginate
from app.models.shippings import InvoicesModel
from app.msmodel.shippingmodel import  Shippingmodel
from app.schemas.shippings import InvoicesSchema
from app.schemas.productitems import ProductitemsSchema
from app.service.shippingservice import InvoiceService
from app.validator.shippingvalidater import Invoicevalidator
from flask import jsonify, request, session
from flask_restplus import Resource, fields, Namespace
import validator 
import os
import bcrypt
import json
from app.db import db
import sys, os
from app.models.users import UsersModel 
from app.helper.decorator import decorator
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
from app.helper.errorhandling import Errorhandling

SHIPPINGS_NOT_FOUND = "No Invoice found."
SHIPPING_NOT_FOUND = "Invoice Not found."
 
 
shipping_ns = Namespace('shipping', description='Invoice related operations')
shippings_ns = Namespace('shippings', description='Invoices related operations')
shipping_nn_ns = Namespace('shipping/new-number', description='Invoice new number operations')

shipping_schema = InvoicesSchema()
shippings_list_schema = InvoicesSchema(many=True)
shippings_pagination = InvoicesPaginate()
shipping_validator = Invoicevalidator()
error_handling = Errorhandling()
product_item = ProductitemsSchema()
shipping_service = InvoiceService()
 
class ShippingsList(Resource):
    shippinglist_args = {
        "filter": fields.Str(required=False),
        "order_by": fields.Str(missing="id",required=False),
        "order_direction": fields.Str(missing="Asc", validate=validate.OneOf(["Asc", "Desc","asc","desc"])),
        "limit": fields.Int(missing=25, required=False),
        "user_id": fields.Int(required=False),
        "page": fields.Int(missing=1, required=False),
        "active": fields.Str(
            missing="all", validate=validate.OneOf(["active", "inactive" , "all"])
        )
    }
    @decorator(permission='COMPANY_ADMIN')
    @use_kwargs(shippinglist_args, location="query")
    @shippings_ns.doc('Get all the Invoices')
    def get(self, **kwargs):
        filter_data = {}
        if "order_direction" in kwargs:
            order_direction = kwargs['order_direction']
        
        if "order_by" in kwargs:
            order_by = kwargs['order_by']
        if "user_id" in kwargs:
            user_id = kwargs['user_id']
            filter_data["user_id"] = user_id
        if  kwargs['active'] != "all":
            active = kwargs['active']
            filter_data["active"] = active
        
        
        if "filter" in kwargs:
            filter_data["filter"] = kwargs['filter']
        
        shippings = InvoicesModel.find_all_by_filter(filter_data, order_by, order_direction)
        if len(shippings) == 0:
            return {'message':  SHIPPINGS_NOT_FOUND}, 404
        shipping_list = shippings_list_schema.dump(shippings)
        
        
        shippings = shippings_pagination.paginator(shipping_list, kwargs['page'], kwargs['limit'],  len(shipping_list))
        return shippings, 200

 

class Shipping(Resource):
    @decorator(permission='COMPANY_ADMIN') 
    @shipping_ns.doc('Get Invoice Detail')
    def get(self, id):
        shipping = InvoicesModel.find_by_id(id)
         
        if shipping:
            shipping = shipping_schema.dump(shipping)
            return shipping 
        return {'message':  SHIPPINGS_NOT_FOUND}, 404

    @decorator(permission='COMPANY_ADMIN') 
    @shipping_ns.doc('Create a Shipping')
    def post(self):
        data = request.get_json(force=True)
            
        rule = shipping_validator.rule()
        
        result, req_obj, errors = validator.validate(data, rule, return_info=True)
        
        if result == False:
            error = error_handling.error(errors, data)
            return error, 400  

        shipping_data = Shippingmodel(**data)
        add_shipping = shipping_service.create(shipping_data)

        if add_shipping:
            return shipping_schema.dump(add_shipping)

        return {'message':  'Unable to save Shipping'}, 400  
     


 