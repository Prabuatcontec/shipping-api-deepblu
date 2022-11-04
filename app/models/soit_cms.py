from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SoitcmsModel(db.Model):
    __bind_key__ = 'db_deepblu_digest'
    __tablename__ = "SOIT_CMS"

    id = db.Column(db.Integer, primary_key=True, name="SOIT_Id")
    shipId = db.Column(db.String(50), nullable=False, name="SOIT_ShipId")
    user  = db.Column(db.String(50), nullable=False, name="SOIT_User")
    shipDivId = db.Column(db.Integer, nullable=False, name="SOIT_ShipDivId")
    shipWhse = db.Column(db.String(50), nullable=False, name="SOIT_ShipWhse")
    shipSite = db.Column(db.String(20), nullable=False, name="SOIT_ShipSite")
    courierMethodId = db.Column(db.Integer, nullable=True, name="SOIT_CourierMethodId")
    trackId = db.Column(db.String(75), name="SOIT_TrackId")
    weight = db.Column(db.Float(precision=None, asdecimal=False, decimal_return_scale=2), name="SOIT_Weight")
    cost = db.Column(db.String(10), name="SOIT_Cost")
    void =  db.Column(db.Boolean, nullable=False, name="SOIT_Void")
    response = db.Column(db.Text, name="SOIT_Response")
    posted = db.Column(db.Boolean, name="SOIT_Posted")
    debug = db.Column(db.Text, name="SOIT_Debug")
    timeStamp = db.Column(db.Datetime, name="SOIT_TimeStamp")
    retries = db.Column(db.Integer, name="SOIT_Retries")
    station = db.Column(db.String(75), name="SOIT_Station")
    build_on_ship = db.Column(db.String(50), name="SOIT_RLSTrackId") 
    processTime = db.Column(db.Datetime, name="SOIT_ProcessTime")
    postedTime = db.Column(db.Datetime, name="SOIT_PostedTime")
    cartonType = db.Column(db.String(25), name="SOIT_CartonType")
    correctAddr = db.Column(db.String(255), name="SOIT_CorrectAddr")
    correctAddr1 = db.Column(db.String(100), name="SOIT_CorrectAddr1")
    build_on_ship = db.Column(db.String(109), name="SOIT_CorrectAddr2")
    correctCity = db.Column(db.String(50), name="SOIT_CorrectCity")
    correctState = db.Column(db.String(50), name="SOIT_CorrectState")
    correctPostalCode = db.Column(db.String(50), name="SOIT_CorrectPostalCode")
    correctCountry = db.Column(db.String(2), name="SOIT_CorrectCountry")
    satDelivery = db.Column(db.Boolean, name="SOIT_SatDelivery")
    

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
    def find_by_id(cls, _id) -> "SoitcmsModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SoitcmsModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
