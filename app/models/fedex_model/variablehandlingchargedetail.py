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
    





class VariableHandlingChargeDetailModel(Model):
    rateType = Column(String(100), nullable=False)
    percentValue = Column(Float(precision=None, asdecimal=False, decimal_return_scale=2), nullable=False)
    fixedValue = relationship("FixedValueModel") 
    rateLevelType = Column(String(100), nullable=False) 
    rateElementBasis = Column(String(100), nullable=False)

    def __repr__(self):
        return self.rateType
 