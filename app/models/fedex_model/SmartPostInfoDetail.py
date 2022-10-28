import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY, Float
from sqlalchemy.orm import relationship
from app.models.fedex.accountnumber import AccountNumberModel
from app.models.fedex.address import AddressModel
from app.models.fedex.contact import ContactModel
from app.models.fedex.emailnotificationrecipients import EmailNotificationRecipientsModel
from app.models.fedex.fixedvalue import FixedValueModel
from app.models.fedex.tins import TinsModel
from flask_appbuilder import Model\
    





class SmartPostInfoDetailModel(Model):
    ancillaryEndorsement = Column(String(100), nullable=False) 
    hubId = Column(String(100), nullable=False) 
    indicia = Column(String(100), nullable=False)
    specialServices = Column(String(100), nullable=False)

    def __repr__(self):
        return self.ancillaryEndorsement
 