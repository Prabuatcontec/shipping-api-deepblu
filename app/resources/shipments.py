


import requests
import os
from app.service.fedex_shipment import FedexshipmentService


from flask import request
from flask_restplus import Resource, fields, Namespace
import datetime
import jwt
from flask_api import status
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.backends import default_backend
import bcrypt
from app.models.users import UsersModel
from app.schemas.users import UsersSchema
import os
USER_NOT_FOUND = "User not found."
USER_ALREADY_EXISTS = "User '{}' Already exists."

shipment_fedex_ns = Namespace('shipment/fedex', description='Shipment')

user_schema = UsersSchema()
users_list_schema = UsersSchema(many=True)
fedex_shipment_service = FedexshipmentService()

class Shipmentfedex(Resource):
    @shipment_fedex_ns.doc('Fedex Shipment')
    def post(self):
        data = request.get_json(force=True)
        if data:            
            try:
              shipment = fedex_shipment_service.shipment(data)  
                
            except Exception as e:
                return e
        else: 
            validation = True
        if validation == True:
            return { "code": status.HTTP_400_BAD_REQUEST, "message": "Bad credentials" }, status.HTTP_400_BAD_REQUEST