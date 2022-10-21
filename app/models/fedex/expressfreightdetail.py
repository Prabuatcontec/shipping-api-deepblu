import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from app.models.fedex.accountnumber import AccountNumberModel
from app.models.fedex.address import AddressModel
from app.models.fedex.contact import ContactModel
from app.models.fedex.emailnotificationrecipients import EmailNotificationRecipientsModel
from app.models.fedex.tins import TinsModel
from flask_appbuilder import Model





class ExpressFreightDetailModel(Model):
    bookingConfirmationNumber = Column(String(100), nullable=False)
    shippersLoadAndCount = Column(Integer, nullable=False)
    packingListEnclosed = Column(Boolean, nullable=False) 

    def __repr__(self):
        return self.address
 