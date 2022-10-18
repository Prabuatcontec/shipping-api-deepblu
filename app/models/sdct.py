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

    id = db.Column(db.Integer, primary_key=True, name="SDCT_ID")
    ship_id = db.Column(db.String(50), nullable=False, name="SDCT_ShipID")
    order_id = db.Column(db.String(25), nullable=False, name="SDCT_OrderID")
    order_line_id = db.Column(db.Integer, nullable=False, name="SDCT_OrderLineID")
    ship_line_id = db.Column(db.Integer, nullable=False, name="SDCT_ShipLineID")
    unit_number = db.Column(db.Integer, nullable=False, name="SDCT_UnitNumber")
    label = db.Column(db.String(50), nullable=False, name="SDCT_Label")
    data = db.Column(db.String(50), nullable=False, name="SDCT_Data")
    status = db.Column(db.Integer, nullable=False, name="SDCT_Status")
    custom_ref = db.Column(db.Integer, name="SDCT_CustomRef")
    add_date = db.Column(db.String(10), name="SDCT_AddDate")
    add_time = db.Column(db.String(8), name="SDCT_AddTime")
    add_user =  db.Column(db.String(15), nullable=False, name="SDCT_AddUser")
    sort_order = db.Column(db.Integer, name="SDCT_SortOrder")
    device_type = db.Column(db.String(50), name="SDCT_DeviceType")
    alt_name = db.Column(db.String(20), name="SDCT_AltName")
    errors = db.Column(db.Integer, name="SDCT_Errors")
    scan_type = db.Column(db.Integer, name="SDCT_ScanType") 
    

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
    
    @classmethod
    def find_all_by_filter(cls, filter, order_by, order_direction) -> List["SdctModel"]: 
            filters = [getattr(cls, attribute) == value for attribute, value in filter.items()] 
            print(filters)
            direction = desc if order_direction == 'desc' else asc
            return cls.query.filter(and_(*filters)).order_by(direction(getattr(cls, order_by))).all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
