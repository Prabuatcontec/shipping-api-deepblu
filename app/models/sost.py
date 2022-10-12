from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SostModel(db.Model):
    __tablename__ = "SOST"

    SOST_ID = db.Column(db.Integer, primary_key=True)
    SOST_BatchID = db.Column(db.Integer, nullable=False)
    SOST_OrderID  = db.Column(db.Integer, nullable=False)
    SOST_ShipID = db.Column(db.String(50), nullable=False)
    SOST_CourierMethodID = db.Column(db.Integer, nullable=False)
    SOST_ShipDivID = db.Column(db.Integer, nullable=False)
    SOST_ThirdPartyAcct = db.Column(db.String(50), nullable=False)
    SOST_ShipWarehouse = db.Column(db.String(25))
    SOST_CustomRef = db.Column(db.Integer)
    SOST_ShipDate = db.Column(db.String(10))
    SOST_ShipTime =  db.Column(db.String(8))
    SOST_ShipUser = db.Column(db.String(15))
    SOST_Status = db.Column(db.Integer)
    SOST_PackSlipPrinted = db.Column(db.Integer)
    SOST_AddUser = db.Column(db.String(15))
    SOST_AddDate = db.Column(db.String(10))
    SOST_AddTime = db.Column(db.String(8))
    SOST_LastChangedUser = db.Column(db.String(15))
    SOST_LastChangedDate = db.Column(db.String(50))
    SOST_LastChangedTime = db.Column(db.String(50))
    SOST_Emailed = db.Column(db.Integer)
    SOST_Posted = db.Column(db.Integer)
    SOST_PostedDate = db.Column(db.String(10))
    SOST_PostedTime = db.Column(db.String(8))
    SOST_CourierPickupDate = db.Column(db.String(10))
    SOST_PostbackDelay = db.Column(db.Integer)
    SOST_PostbackStarted = db.Column(db.Integer) 
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'SostModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "SostModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SostModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
