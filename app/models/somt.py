from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SomtModel(db.Model):
    __tablename__ = "SOMT"

    SOMT_ID = db.Column(db.Integer, primary_key=True)
    SOMT_BatchID = db.Column(db.Integer, nullable=False)
    SOMT_OrderID  = db.Column(db.Integer, nullable=False)
    SOMT_CusOrderID = db.Column(db.String(50), nullable=False)
    SOMT_CusPOID = db.Column(db.String(50), nullable=False)
    SOMT_ShipAcct = db.Column(db.String(100), nullable=False)
    SOMT_ShipDivID = db.Column(db.Integer, nullable=False)
    SOMT_CourierMethodID = db.Column(db.Integer)
    SOMT_ThirdPartyAcct = db.Column(db.String(50))
    SOMT_ShipSpecialIns = db.Column(db.String(250))
    SOMT_MsgToCourier =  db.Column(db.String(50))
    SOMT_PackslipMsg = db.Column(db.String(250))
    SOMT_ShipToCompany = db.Column(db.String(75))
    SOMT_ShipToName = db.Column(db.String(80))
    SOMT_ShipToAddr1 = db.Column(db.String(100))
    SOMT_ShipToAddr2 = db.Column(db.String(100))
    SOMT_ShipToCity = db.Column(db.String(50))
    SOMT_ShipToState = db.Column(db.String(50))
    SOMT_ShipToPostalCode = db.Column(db.String(50))
    SOMT_ShipToCountry = db.Column(db.String(2))
    SOMT_ShipToPhone = db.Column(db.String(50))
    SOMT_ShipToEmail = db.Column(db.String(50))
    SOMT_ShipToFax = db.Column(db.String(50))
    SOMT_ReturnToName = db.Column(db.String(50))
    SOMT_ReturnToCompany = db.Column(db.String(50))
    SOMT_ReturnToAddr1 = db.Column(db.String(50))
    SOMT_ReturnToAddr2 = db.Column(db.String(50))
    SOMT_ReturnToCity = db.Column(db.String(50))
    SOMT_ReturnToState = db.Column(db.String(50))
    SOMT_ReturnToCountry = db.Column(db.String(50))
    SOMT_ReturnToPostalCode = db.Column(db.String(50))
    SOMT_Status = db.Column(db.Integer)
    SOMT_MsgToWarehouse = db.Column(db.String(250))
    SOMT_MsgToWarehouse = db.Column(db.String(10))
    SOMT_RecWarehouse = db.Column(db.String(25))
    SOMT_CustomRef = db.Column(db.Integer)
    SOMT_LastChangedDate = db.Column(db.String(10))
    SOMT_LastChangedTime = db.Column(db.String(8))
    SOMT_LastChangedUser = db.Column(db.String(15))
    SOMT_AddDate = db.Column(db.String(10))
    SOMT_AddTime = db.Column(db.String(8))
    SOMT_AddUser = db.Column(db.String(15))
    SOMT_BillToCompany = db.Column(db.String(75))
    SOMT_BillToName = db.Column(db.String(75))
    SOMT_BillToAddr1 = db.Column(db.String(50))
    SOMT_BillToAddr2 = db.Column(db.String(50))
    SOMT_BillToAddr3 = db.Column(db.String(50))
    SOMT_BillToCity = db.Column(db.String(50))
    SOMT_BillToState = db.Column(db.String(50))
    SOMT_BillToCountry = db.Column(db.String(50))
    SOMT_BillToPostalCode = db.Column(db.String(50))
    SOMT_BillToRef1 = db.Column(db.String(20))
    SOMT_ShipCounter = db.Column(db.Integer)
    SOMT_Reported = db.Column(db.Integer)
    SOMT_QtyType = db.Column(db.String(20))
    SOMT_Channel = db.Column(db.String(20))
    SOMT_Marker = db.Column(db.Integer)
    SOMT_SLADate = db.Column(db.String(10))
    SOMT_OrigRecWarehouse = db.Column(db.String(25))
    SOMT_OrigSLADate = db.Column(db.String(10))
    SOMT_Priority = db.Column(db.Integer)
    SOMT_RcvdDate = db.Column(db.String(10))
    SOMT_RcvdTime = db.Column(db.String(8))
    SOMT_OrigCourierMethodID = db.Column(db.Integer)
    SOMT_Reason = db.Column(db.Integer)
    SOMT_ChargeRFulfillment = db.Column(db.Integer)
    SOMT_NoInvoice = db.Column(db.Integer)
    SOMT_ChargeRScrap = db.Column(db.Integer)
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'SomtModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "SomtModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SomtModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
