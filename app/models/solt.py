from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SoltModel(db.Model):
    __tablename__ = "SOLT"

    SOLT_ID = db.Column(db.Integer, primary_key=True)
    SOLT_BatchID = db.Column(db.Integer, nullable=False)
    SOLT_OrderID  = db.Column(db.Integer, nullable=False)
    SOLT_OrderLineID = db.Column(db.Integer, nullable=False)
    SOLT_ItemID = db.Column(db.String(25), nullable=False)
    SOLT_CusItemID = db.Column(db.String(100), nullable=False)
    SOLT_CusItemName = db.Column(db.String(100), nullable=True)
    SOLT_Qty = db.Column(db.Integer)
    SOLT_Status = db.Column(db.Integer)
    SOLT_CustomRef = db.Column(db.Integer)
    SOLT_Type =  db.Column(db.Integer, nullable=False)
    SOLT_AddDate = db.Column(db.Date)
    SOLT_AddTime = db.Column(db.String(15))
    SOLT_AddUser = db.Column(db.String(255))
    SOLT_PhantomItemName = db.Column(db.String(100))
    SOLT_Marker = db.Column(db.Integer)
    SOLT_SubAssemItemID = db.Column(db.String(30))
    SOLT_BuildOnShip = db.Column(db.Integer)
    SOLT_SyncKey = db.Column(db.Integer)
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'SoltModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "SoltModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SoltModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
