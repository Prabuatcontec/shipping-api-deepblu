import imp
from app.helper.shippingdatapagination import ShippingdataPaginate
from app.models.sdct import SdctModel 
from app.msmodel.shippingmodel import  Shippingmodel
from app.schemas.shipping import ShippingdataSchema
from app.service.shippingservice import ShippingService 
from app.validator.shippingvalidater import Shippingvalidater
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

SHIPPINGS_DATA_NOT_FOUND = "No Shipping data found."
SHIPPING_DATA_NOT_FOUND = "Invoice Not found."
 
 
shipping_data_ns = Namespace('shipping-data', description='Shipping data related operations')
shipping_datas_ns = Namespace('shipping-datas', description='Shipping datas related operations') 

shipping_schema = ShippingdataSchema()
shippings_list_schema = ShippingdataSchema(many=True)
shippings_pagination = ShippingdataPaginate()
shipping_validator = Shippingvalidater()
error_handling = Errorhandling() 

shipping_service = ShippingService()

class ShippingsdataList(Resource):
    shippinglist_args = {
        "filter": fields.Str(required=False),
        "order_by": fields.Str(missing="SDCT_ID",required=False),
        "order_direction": fields.Str(missing="Asc", validate=validate.OneOf(["Asc", "Desc","asc","desc"])),
        "limit": fields.Int(missing=25, required=False),
        "ship_id": fields.Int(required=False),
        "page": fields.Int(missing=0, required=False),
        "active": fields.Str(
            missing="all", validate=validate.OneOf(["active", "inactive" , "all"])
        )
    } 
    @use_kwargs(shippinglist_args, location="query")
    @shipping_datas_ns.doc('Get all shipping data')
    def get(self, **kwargs):
        filter_data = {}
        if "order_direction" in kwargs:
            order_direction = kwargs['order_direction']
        
        if "order_by" in kwargs:
            order_by = kwargs['order_by']
        if "ship_id" in kwargs:
            ship_id = kwargs['ship_id']
            filter_data["ship_id"] = ship_id
        if  kwargs['active'] != "all":
            active = kwargs['active']
            filter_data["active"] = active
        
        
        if "filter" in kwargs:
            filter_data["filter"] = kwargs['filter']
        
        shippings = SdctModel.find_all_by_filter(filter_data, order_by, order_direction)
        if len(shippings) == 0:
            return {'message':  SHIPPINGS_DATA_NOT_FOUND}, 404
        shipping_list = shippings_list_schema.dump(shippings)
        
        
        shippings = shippings_pagination.paginator(shipping_list, kwargs['page'], kwargs['limit'],  len(shipping_list))
        return shippings, 200

 

class Shippingdata(Resource): 
    @shipping_data_ns.doc('Get Shipping Detail')
    def get(self, id):
        shipping = SdctModel.find_by_id(id)
         
        if shipping:
            shipping = shipping_schema.dump(shipping)
            return shipping 
        return {'message':  SHIPPINGS_DATA_NOT_FOUND}, 404
 
    @shipping_data_ns.doc('Create a Shipping')
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

        return {'message':  'Unable to save Shipping data'}, 400  
     


 