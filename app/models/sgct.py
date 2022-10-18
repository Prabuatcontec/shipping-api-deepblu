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

    id = db.Column(db.Integer, primary_key=True, name="SGCT_ID")
    link_table = db.Column(db.String(50), nullable=False, name="SGCT_LinkTable")
    link_id = db.Column(db.String(25), name="SGCT_LinkID")
    label = db.Column(db.String(25), nullable=True, name="SGCT_Label")
    value = db.Column(db.String(1024), nullable=True, name="SGCT_Value")
    unit_number = db.Column(db.Integer, nullable=True, name="SGCT_UnitNumber") 
    batch_id = db.Column(db.String(10), name="SGCT_BatchID")
    order_id = db.Column(db.String(8), name="SGCT_OrderID")
    order_line_id =  db.Column(db.String(15), nullable=False, name="SGCT_OrderLineID")
    add_date = db.Column(db.Integer, name="SGCT_AddDate")
    add_time = db.Column(db.String(50), name="SGCT_AddTime")
    

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
