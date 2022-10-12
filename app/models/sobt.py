from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SobtModel(db.Model):
    __tablename__ = "SGCT"

    SOBT_ID = db.Column(db.Integer, primary_key=True)
    SOBT_BatchID = db.Column(db.String(50), nullable=False)
    SOBT_CusDivID = db.Column(db.Integer, nullable=False)
    SOBT_Status = db.Column(db.Integer, nullable=False)
    SOBT_OrderType = db.Column(db.Integer, nullable=False)
    SOBT_CustomRef = db.Column(db.Integer, nullable=True)
    SOBT_LastChangedDate = db.Column(db.String(10))
    SOBT_LastChangedTime = db.Column(db.String(8))
    SOBT_LastChangedUser = db.Column(db.String(15))
    SOBT_AddDate =  db.Column(db.String(10), nullable=False)
    SOBT_AddTime = db.Column(db.String(8))
    SOBT_AddUser = db.Column(db.String(15))
    SOBT_SortDesc = db.Column(db.String(255))
    SOBT_Marker = db.Column(db.Integer)
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'SobtModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "SobtModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SobtModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
