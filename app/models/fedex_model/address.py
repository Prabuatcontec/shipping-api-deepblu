import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class AddressModel(Model):
    streetLines = Column(ARRAY,  nullable=False)
    city = Column(String(50), nullable=False)
    stateOrProvinceCode = Column(String(5), nullable=False)
    postalCode = Column(String(10), nullable=False)
    countryCode  = Column(String(5), nullable=False)
    residential = Column(Boolean, nullable=False) 

    def __repr__(self):
        return self.streetLines 