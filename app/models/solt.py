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

    id = db.Column(db.Integer, primary_key=True, name="SOLT_ID")
    batch_id = db.Column(db.Integer, nullable=False, name="SOLT_BatchID")
    order_id  = db.Column(db.Integer, nullable=False, name="SOLT_OrderID")
    order_line_id = db.Column(db.Integer, nullable=False, name="SOLT_OrderLineID")
    item_id = db.Column(db.String(25), nullable=False, name="SOLT_ItemID")
    cus_item_id = db.Column(db.String(100), nullable=False, name="SOLT_CusItemID")
    cus_item_name = db.Column(db.String(100), nullable=True, name="SOLT_CusItemName")
    qty = db.Column(db.Integer, name="SOLT_Qty")
    status = db.Column(db.Integer, name="SOLT_Status")
    custom_ref = db.Column(db.Integer, name="SOLT_CustomRef")
    type =  db.Column(db.Integer, nullable=False, name="SOLT_Type")
    add_date = db.Column(db.Date, name="SOLT_AddDate")
    add_time = db.Column(db.String(15), name="SOLT_AddTime")
    add_user = db.Column(db.String(255), name="SOLT_AddUser")
    phatom_item_name = db.Column(db.String(100), name="SOLT_PhantomItemName")
    marker = db.Column(db.Integer, name="SOLT_Marker")
    sub_addem_item_id = db.Column(db.String(30), name="SOLT_SubAssemItemID")
    build_on_ship = db.Column(db.Integer, name="SOLT_BuildOnShip")
    sync_key = db.Column(db.Integer, name="SOLT_SyncKey")
    

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
