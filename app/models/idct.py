from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class IdctModel(db.Model):
    __bind_key__ = 'db_deepblu'
    __tablename__ = "IDCT"

    IDCT_ID = db.Column(db.Integer, primary_key=True)
    IDCT_ItemID = db.Column(db.String(25), nullable=True)
    IDCT_Label  = db.Column(db.String(25), nullable=True) 
    IDCT_MinLength = db.Column(db.Integer, nullable=True)
    IDCT_MaxLength = db.Column(db.Integer, nullable=True)
    IDCT_RegExp = db.Column(db.String(50), nullable=True)
    IDCT_SortOrder = db.Column(db.Integer)
    IDCT_Desc = db.Column(db.String(100))
    IDCT_AltName = db.Column(db.String(20))
    IDCT_AltName2 =  db.Column(db.String(20))
    IDCT_DeviceType = db.Column(db.String(50))
    IDCT_AltMake = db.Column(db.String(30))
    IDCT_AltModel = db.Column(db.String(30))
    IDCT_AltMake2 = db.Column(db.String(15))
    IDCT_AltModel2 = db.Column(db.String(30))
    IDCT_UseOnShip = db.Column(db.Integer)
    IDCT_UseOnRelabel = db.Column(db.Integer)
    IDCT_UseOnRMA = db.Column(db.Integer)
    IDCT_UseOnReceive = db.Column(db.Integer)
    IDCT_IgnoreDups  = db.Column(db.Integer)
    IDCT_Master = db.Column(db.Integer)
    IDCT_EISDeviceType = db.Column(db.String(50))
    IDCT_EISModel = db.Column(db.String(50))
    IDCT_EISField = db.Column(db.String(20))
    IDCT_AddDate = db.Column(db.String(20))
    IDCT_AddTime = db.Column(db.String(20))
    IDCT_RealDeviceType = db.Column(db.String(50))
    IDCT_BillerMac = db.Column(db.Integer)
    IDCT_EmmRequest = db.Column(db.Integer) 
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'IdctModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "IdctModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["IdctModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
