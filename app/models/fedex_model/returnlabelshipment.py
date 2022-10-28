import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class LabelResponseOptions(Model):
    labelResponseOptions = Column(String(50), unique=True, nullable=False)
    requestedShipment = relationship("RequestedShipment")

    def __repr__(self):
        return self.name

class ShippingChargesPayment(Model):
    paymentType = Column(String(50), unique=True, nullable=False)

class ShipmentSpecialServices(Model):
    specialServiceTypes = Column(ARRAY, unique=True, nullable=False)

class RequestedShipment(Model):
    id = Column(Integer, primary_key=True)
    shipDatestamp = Column(String(50),  nullable=False)
    serviceType = Column(String(50),   nullable=False)
    packagingType = Column(String(50),   nullable=False)
    pickupType = Column(String(50),  nullable=False)
    blockInsightVisibility = Column(Boolean,   nullable=False)
    shippingChargesPayment = relationship("ShippingChargesPayment")

    def __repr__(self):
        return self.name


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class AccountNumber(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    begin_date = Column(Date, default=today, nullable=False)
    end_date = Column(Date, nullable=True)

    def __repr__(self):
        return self.full_name