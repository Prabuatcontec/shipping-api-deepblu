import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from app.models.fedex.address import AddressModel
from app.models.fedex.contact import ContactModel
from app.models.fedex.tins import TinsModel
from flask_appbuilder import Model



class SoldtoModel(Model):
    address = relationship("AddressModel")
    contact = relationship("ContactModel")
    tins = relationship("TinsModel")
    accountNumber = relationship("ValueModel")

    def __repr__(self):
        return self.address

class ValueModel(Model):
    value = Column(String(50), unique=True, nullable=False) 

    def __repr__(self):
        return self.value