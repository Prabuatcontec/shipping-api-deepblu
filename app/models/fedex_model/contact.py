import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class ContactModel(Model):
    personName = Column(String(50), nullable=False)
    emailAddress = Column(String(100), nullable=False)
    phoneExtension = Column(String(5), nullable=False)
    phoneNumber  = Column(String(15), nullable=False)
    companyName = Column(String(150), nullable=True) 
    faxNumber = Column(String(20), nullable=True)

    def __repr__(self):
        return self.streetLines 