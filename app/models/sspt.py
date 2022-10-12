from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SsptModel(db.Model):
    __tablename__ = "SSPT"

    SSPT_ID = db.Column(db.Integer, primary_key=True)
    SSPT_BatchID = db.Column(db.Integer, nullable=False)
    SSPT_OrderID  = db.Column(db.Integer, nullable=False)
    SSPT_ShipID = db.Column(db.String(50), nullable=False)
    SSPT_ComInvoice = db.Column(db.Integer, nullable=False)
    SSPT_Weight = db.Column(db.Float(precision=None, asdecimal=False, decimal_return_scale=2), nullable=False)
    SSPT_Cost = db.Column(db.Float(precision=None, asdecimal=False, decimal_return_scale=2), nullable=False)
    SSPT_CostByTotal = db.Column(db.Integer)
    SSPT_TrackID = db.Column(db.String(75))
    SSPT_RMAID = db.Column(db.String(25))
    SSPT_RMADate =  db.Column(db.Datetime)
    SSPT_ShipDivID = db.Column(db.Integer)
    SSPT_CourierMethodID = db.Column(db.Integer)
    SSPT_ThirdPartyAcct = db.Column(db.String(50))
    SSPT_AddUser = db.Column(db.String(15))
    SSPT_AddDate = db.Column(db.String(10))
    SSPT_AddTime = db.Column(db.String(8))
    SSPT_Status = db.Column(db.Integer)
    SSPT_ManifestControlled = db.Column(db.Integer)
    SSPT_CourierDeliveredDate = db.Column(db.String(10))
    SSPT_CourierStatus = db.Column(db.String(50))
    SSPT_CourierStatusType = db.Column(db.String(1))
    SSPT_CourierUpdateDate = db.Column(db.String(10))
    SSPT_RLSTrackID = db.Column(db.String(75))
    SSPT_AltPackageID = db.Column(db.String(20))
    SSPT_CartonItemID = db.Column(db.String(25))
    SSPT_Station = db.Column(db.String(20)) 
    SSPT_QCStatus = db.Column(db.Integer)
    SSPT_SatDelivery = db.Column(db.String(1))
    SSPT_PalletCount = db.Column(db.Integer)
    SSPT_PalletMultipleSKUCount = db.Column(db.Integer)
    SSPT_CartonBoxCount = db.Column(db.Integer) 
    SSPT_MultiSkuType = db.Column(db.String(10)) 
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'SsptModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "SsptModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SsptModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
