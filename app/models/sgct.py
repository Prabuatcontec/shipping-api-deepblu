from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SgctModel(db.Model):
    __tablename__ = "SGCT"

    SGCT_ID = db.Column(db.Integer, primary_key=True)
    SGCT_LinkTable = db.Column(db.String(50), nullable=False)
    SGCT_LinkID = db.Column(db.String(25))
    SGCT_Label = db.Column(db.String(25), nullable=True)
    SGCT_Value = db.Column(db.String(1024), nullable=True)
    SGCT_UnitNumber = db.Column(db.Integer, nullable=True)
    SGCT_TheOtherWhiteMeat = db.Column(db.Integer)
    SGCT_BatchID = db.Column(db.String(10))
    SGCT_OrderID = db.Column(db.String(8))
    SGCT_OrderLineID =  db.Column(db.String(15), nullable=False)
    SGCT_AddDate = db.Column(db.Integer)
    SGCT_AddTime = db.Column(db.String(50))
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'SgctModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "SgctModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SgctModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
