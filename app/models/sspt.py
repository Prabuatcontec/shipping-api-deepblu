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

    id = db.Column(db.Integer, primary_key=True, name="SSPT_ID")
    batch_id = db.Column(db.Integer, nullable=False, name="SSPT_BatchID")
    order_id  = db.Column(db.Integer, nullable=False, name="SSPT_OrderID")
    ship_id = db.Column(db.String(50), nullable=False, name="SSPT_ShipID")
    com_invoice = db.Column(db.Integer, nullable=False, name="SSPT_ComInvoice")
    weight = db.Column(db.Float(precision=None, asdecimal=False, decimal_return_scale=2), nullable=False, name="SSPT_Weight")
    cost = db.Column(db.Float(precision=None, asdecimal=False, decimal_return_scale=2), nullable=False, name="SSPT_Cost")
    cost_by_total = db.Column(db.Integer, name="SSPT_CostByTotal")
    track_id = db.Column(db.String(75), name="SSPT_TrackID")
    rma_id = db.Column(db.String(25), name="SSPT_RMAID")
    rma_date =  db.Column(db.Datetime, name="SSPT_RMADate")
    ship_div_id = db.Column(db.Integer, name="SSPT_ShipDivID")
    courier_method_id = db.Column(db.Integer, name="SSPT_CourierMethodID")
    third_party_acct = db.Column(db.String(50), name="SSPT_ThirdPartyAcct")
    add_user = db.Column(db.String(15), name="SSPT_AddUser")
    add_date = db.Column(db.String(10), name="SSPT_AddDate")
    add_time = db.Column(db.String(8), name="SSPT_AddTime")
    status = db.Column(db.Integer, name="SSPT_Status")
    manifest_controlled = db.Column(db.Integer, name="SSPT_ManifestControlled")
    courier_delivery_date = db.Column(db.String(10), name="SSPT_CourierDeliveredDate")
    courier_status = db.Column(db.String(50), name="SSPT_CourierStatus")
    courier_status_type = db.Column(db.String(1), name="SSPT_CourierStatusType")
    courier_update_date = db.Column(db.String(10), name="SSPT_CourierUpdateDate")
    rls_track_id = db.Column(db.String(75), name="SSPT_RLSTrackID")
    alt_package_id = db.Column(db.String(20), name="SSPT_AltPackageID")
    carton_item_id = db.Column(db.String(25), name="SSPT_CartonItemID")
    station = db.Column(db.String(20), name="SSPT_Station") 
    qc_status = db.Column(db.Integer, name="SSPT_QCStatus")
    sat_delivery = db.Column(db.String(1), name="SSPT_SatDelivery")
    pallet_count = db.Column(db.Integer, name="SSPT_PalletCount")
    pallet_multiple_sku_count = db.Column(db.Integer, name="SSPT_PalletMultipleSKUCount")
    carton_box_count = db.Column(db.Integer, name="SSPT_CartonBoxCount") 
    multi_sku_type = db.Column(db.String(10), name="SSPT_MultiSkuType") 
    

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
