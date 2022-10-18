from operator import and_
from app.db import db
from typing import List
import datetime 
from flask import session, request
import jwt
import os
from functools import wraps
from sqlalchemy import asc, and_, desc


class SomtModel(db.Model):
    __tablename__ = "SOMT"

    id = db.Column(db.Integer, primary_key=True, name="SOMT_ID")
    batch_id = db.Column(db.Integer, nullable=False, name="SOMT_BatchID")
    order_id  = db.Column(db.Integer, nullable=False, name="SOMT_OrderID")
    cus_order_id = db.Column(db.String(50), nullable=False, name="SOMT_CusOrderID")
    cus_po_id = db.Column(db.String(50), nullable=False, name="SOMT_CusPOID")
    ship_acct = db.Column(db.String(100), nullable=False, name="SOMT_ShipAcct")
    ship_div_id = db.Column(db.Integer, nullable=False, name="SOMT_ShipDivID")
    courier_method_id = db.Column(db.Integer, name="SOMT_CourierMethodID")
    third_party_acct = db.Column(db.String(50), name="SOMT_ThirdPartyAcct")
    ship_special_ins = db.Column(db.String(250), name="SOMT_ShipSpecialIns")
    msg_to_courier =  db.Column(db.String(50), name="SOMT_MsgToCourier")
    pack_slip_msg = db.Column(db.String(250), name="SOMT_PackslipMsg")
    ship_to_company = db.Column(db.String(75), name="SOMT_ShipToCompany")
    ship_to_name = db.Column(db.String(80), name="SOMT_ShipToName")
    ship_to_addr1 = db.Column(db.String(100), name="SOMT_ShipToAddr1")
    ship_to_addr2 = db.Column(db.String(100), name="SOMT_ShipToAddr2")
    ship_to_city = db.Column(db.String(50), name="SOMT_ShipToCity")
    ship_to_state = db.Column(db.String(50), name="SOMT_ShipToState")
    ship_to_postal_code = db.Column(db.String(50), name="SOMT_ShipToPostalCode")
    ship_to_country = db.Column(db.String(2), name="SOMT_ShipToCountry")
    ship_to_phone = db.Column(db.String(50), name="SOMT_ShipToPhone")
    ship_to_email = db.Column(db.String(50), name="SOMT_ShipToEmail")
    ship_to_fax = db.Column(db.String(50), name="SOMT_ShipToFax")
    return_to_name = db.Column(db.String(50), name="SOMT_ReturnToName")
    return_to_company = db.Column(db.String(50), name="SOMT_ReturnToCompany")
    return_to_addr1 = db.Column(db.String(50), name="SOMT_ReturnToAddr1")
    return_to_addr2 = db.Column(db.String(50), name="SOMT_ReturnToAddr2")
    return_to_city = db.Column(db.String(50), name="SOMT_ReturnToCity")
    return_to_state = db.Column(db.String(50), name="SOMT_ReturnToState")
    return_to_country = db.Column(db.String(50), name="SOMT_ReturnToCountry")
    return_to_postal_code = db.Column(db.String(50), name="SOMT_ReturnToPostalCode")
    status = db.Column(db.Integer, name="SOMT_Status")
    msg_to_warehouse = db.Column(db.String(250), name="SOMT_MsgToWarehouse") 
    rec_warehouse = db.Column(db.String(25), name="SOMT_RecWarehouse")
    custom_ref = db.Column(db.Integer, name="SOMT_CustomRef")
    last_changed_date = db.Column(db.String(10), name="SOMT_LastChangedDate")
    last_changed_time = db.Column(db.String(8), name="SOMT_LastChangedTime")
    last_changed_user = db.Column(db.String(15), name="SOMT_LastChangedUser")
    add_date = db.Column(db.String(10), name="SOMT_AddDate")
    add_time = db.Column(db.String(8), name="SOMT_AddTime")
    add_user = db.Column(db.String(15), name="SOMT_AddUser")
    bill_to_company = db.Column(db.String(75), name="SOMT_BillToCompany")
    bill_to_name = db.Column(db.String(75), name="SOMT_BillToName")
    bill_to_addr1 = db.Column(db.String(50), name="SOMT_BillToAddr1")
    bill_to_addr2 = db.Column(db.String(50), name="SOMT_BillToAddr2")
    bill_to_addr3 = db.Column(db.String(50), name="SOMT_BillToAddr3")
    bill_to_city = db.Column(db.String(50), name="SOMT_BillToCity")
    bill_to_state = db.Column(db.String(50), name="SOMT_BillToState")
    bill_to_country = db.Column(db.String(50), name="SOMT_BillToCountry")
    bill_to_postal_code = db.Column(db.String(50), name="SOMT_BillToPostalCode")
    bill_to_ref1 = db.Column(db.String(20), name="SOMT_BillToRef1")
    ship_counter = db.Column(db.Integer, name="SOMT_ShipCounter")
    reported = db.Column(db.Integer, name="SOMT_Reported")
    qty_type = db.Column(db.String(20), name="SOMT_QtyType")
    channel = db.Column(db.String(20), name="SOMT_Channel")
    marker = db.Column(db.Integer, name="SOMT_Marker")
    sla_date = db.Column(db.String(10), name="SOMT_SLADate")
    orig_rec_warehouse = db.Column(db.String(25), name="SOMT_OrigRecWarehouse")
    orig_sla_date = db.Column(db.String(10), name="SOMT_OrigSLADate")
    priority = db.Column(db.Integer, name="SOMT_Priority")
    rcvd_date = db.Column(db.String(10), name="SOMT_RcvdDate")
    rcvd_time = db.Column(db.String(8), name="SOMT_RcvdTime")
    orig_courier_method_id = db.Column(db.Integer, name="SOMT_OrigCourierMethodID")
    reason = db.Column(db.Integer, name="SOMT_Reason")
    charger_fulfillment = db.Column(db.Integer, name="SOMT_ChargeRFulfillment")
    no_invoice = db.Column(db.Integer, name="SOMT_NoInvoice")
    charger_scrap = db.Column(db.Integer, name="SOMT_ChargeRScrap")
    

    def __init__(self, **kwargs):   
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0] 
            setattr(self, property, value)

    def __repr__(self):
        return 'SomtModel(id=%d)' % (self.id)

    def json(self):
        return { 
                        "id": self.id 
                    }
 
    @classmethod
    def find_by_id(cls, _id) -> "SomtModel":
        return cls.query.filter_by(id=_id).first()
      
    @classmethod
    def find_all(cls) -> List["SomtModel"]:
        return cls.query.all()
 
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
