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

    id = db.Column(db.Integer, primary_key=True, name="SOST_ID")
    batch_id = db.Column(db.Integer, nullable=False, name="SOST_BatchID")
    order_id  = db.Column(db.Integer, nullable=False, name="SOST_OrderID")
    ship_id = db.Column(db.String(50), nullable=False, name="SOST_ShipID")
    courier_method_id = db.Column(db.Integer, nullable=False, name="SOST_CourierMethodID")
    ship_div_id = db.Column(db.Integer, nullable=False, name="SOST_ShipDivID")
    third_party_Acct = db.Column(db.String(50), nullable=False, name="SOST_ThirdPartyAcct")
    ship_warehouse = db.Column(db.String(25), name="SOST_ShipWarehouse")
    custom_ref = db.Column(db.Integer, name="SOST_CustomRef")
    ship_date = db.Column(db.String(10), name="SOST_ShipDate")
    ship_time =  db.Column(db.String(8), name="SOST_ShipTime")
    ship_user = db.Column(db.String(15), name="SOST_ShipUser")
    status = db.Column(db.Integer, name="SOST_Status")
    pack_slip_printed = db.Column(db.Integer, name="SOST_PackSlipPrinted")
    add_user = db.Column(db.String(15), name="SOST_AddUser")
    add_date = db.Column(db.String(10), name="SOST_AddDate")
    add_time = db.Column(db.String(8), name="SOST_AddTime")
    last_changed_user = db.Column(db.String(15), name="SOST_LastChangedUser")
    last_changed_date = db.Column(db.String(50), name="SOST_LastChangedDate")
    last_changed_time = db.Column(db.String(50), name="SOST_LastChangedTime")
    emailed = db.Column(db.Integer, name="SOST_Emailed")
    posted = db.Column(db.Integer, name="SOST_Posted")
    posted_date = db.Column(db.String(10), name="SOST_PostedDate")
    posted_time = db.Column(db.String(8), name="SOST_PostedTime")
    courier_pickup_date = db.Column(db.String(10), name="SOST_CourierPickupDate")
    postback_delay = db.Column(db.Integer, name="SOST_PostbackDelay")
    postback_started = db.Column(db.Integer, name="SOST_PostbackStarted") 
    

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
