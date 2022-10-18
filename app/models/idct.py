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

    id = db.Column(db.Integer, primary_key=True, name="IDCT_ID")
    item_id = db.Column(db.String(25), nullable=True, name="IDCT_ItemID")
    label  = db.Column(db.String(25), nullable=True, name="IDCT_Label") 
    min_length = db.Column(db.Integer, nullable=True, name="IDCT_MinLength")
    max_length = db.Column(db.Integer, nullable=True, name="IDCT_MaxLength")
    reg_exp = db.Column(db.String(50), nullable=True, name="IDCT_RegExp")
    sort_order = db.Column(db.Integer, name="IDCT_SortOrder")
    desc = db.Column(db.String(100), name="IDCT_Desc")
    alt_name = db.Column(db.String(20), name="IDCT_AltName")
    alt_name2 =  db.Column(db.String(20), name="IDCT_AltName2")
    device_type = db.Column(db.String(50), name="IDCT_DeviceType")
    alt_make = db.Column(db.String(30), name="IDCT_AltMake")
    alt_model = db.Column(db.String(30), name="IDCT_AltModel")
    alt_make2 = db.Column(db.String(15), name="IDCT_AltMake2")
    alt_model2 = db.Column(db.String(30), name="IDCT_AltModel2")
    use_on_ship = db.Column(db.Integer, name="IDCT_UseOnShip")
    use_on_relabel = db.Column(db.Integer, name="IDCT_UseOnRelabel")
    use_on_rma = db.Column(db.Integer, name="IDCT_UseOnRMA")
    use_on_receive = db.Column(db.Integer, name="IDCT_UseOnReceive")
    ignore_dups  = db.Column(db.Integer, name="IDCT_IgnoreDups")
    master = db.Column(db.Integer, name="IDCT_Master")
    eis_device_type = db.Column(db.String(50), name="IDCT_EISDeviceType")
    eis_model = db.Column(db.String(50), name="IDCT_EISModel")
    eis_field = db.Column(db.String(20), name="IDCT_EISField")
    add_date = db.Column(db.String(20), name="IDCT_AddDate")
    add_time = db.Column(db.String(20), name="IDCT_AddTime")
    real_device_type = db.Column(db.String(50), name="IDCT_RealDeviceType")
    biller_mac = db.Column(db.Integer, name="IDCT_BillerMac")
    emm_request = db.Column(db.Integer, name="IDCT_EmmRequest") 
    

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
