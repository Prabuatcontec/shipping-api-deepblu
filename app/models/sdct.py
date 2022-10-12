from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SdctModel(db.Model):
    __tablename__ = "SDCT"

    SDCT_ID = db.Column(db.Integer, primary_key=True)
    SDCT_ShipID = db.Column(db.String(50), nullable=False)
    SDCT_OrderID = db.Column(db.String(25), nullable=False)
    SDCT_OrderLineID = db.Column(db.Integer, nullable=False)
    SDCT_ShipLineID = db.Column(db.Integer, nullable=False)
    SDCT_UnitNumber = db.Column(db.Integer, nullable=False)
    SDCT_Label = db.Column(db.String(50), nullable=False)
    SDCT_Data = db.Column(db.String(50), nullable=False)
    SDCT_Status = db.Column(db.Integer, nullable=False)
    SDCT_CustomRef = db.Column(db.Integer)
    SDCT_AddDate = db.Column(db.String(10))
    SDCT_AddTime = db.Column(db.String(8))
    SDCT_AddUser =  db.Column(db.String(15), nullable=False)
    SDCT_SortOrder = db.Column(db.Integer)
    SDCT_DeviceType = db.Column(db.String(50))
    SDCT_AltName = db.Column(db.String(20))
    SDCT_Errors = db.Column(db.Integer)
    SDCT_ScanType = db.Column(db.Integer) 
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'SdctModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "SdctModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SdctModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
