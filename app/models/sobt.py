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
    __tablename__ = "SOBT"

    id = db.Column(db.Integer, primary_key=True, name="SOBT_ID")
    batch_id = db.Column(db.String(50), nullable=False, name="SOBT_BatchID")
    cus_div_id = db.Column(db.Integer, nullable=False, name="SOBT_CusDivID")
    status = db.Column(db.Integer, nullable=False, name="SOBT_Status")
    order_type = db.Column(db.Integer, nullable=False, name="SOBT_OrderType")
    custom_ref = db.Column(db.Integer, nullable=True, name="SOBT_CustomRef")
    last_changed_date = db.Column(db.String(10), name="SOBT_LastChangedDate")
    last_changed_time = db.Column(db.String(8), name="SOBT_LastChangedTime")
    last_changed_user = db.Column(db.String(15), name="SOBT_LastChangedUser")
    add_date =  db.Column(db.String(10), nullable=False, name="SOBT_AddDate")
    add_time = db.Column(db.String(8), name="SOBT_AddTime")
    add_user = db.Column(db.String(15), name="SOBT_AddUser")
    sort_desc = db.Column(db.String(255), name="SOBT_SortDesc")
    marker = db.Column(db.Integer, name="SOBT_Marker")
    

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
