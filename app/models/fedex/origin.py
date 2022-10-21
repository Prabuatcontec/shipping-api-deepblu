import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from app.models.fedex.address import AddressModel
from app.models.fedex.contact import ContactModel
from flask_appbuilder import Model



class OriginModel(Model):
    address = relationship("AddressModel")
    contact = relationship("ContactModel")

    def __repr__(self):
        return self.streetLines 