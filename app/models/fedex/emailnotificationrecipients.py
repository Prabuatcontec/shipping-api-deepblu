import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from app.models.fedex.payor import PayorModel 
from flask_appbuilder import Model





class EmailNotificationRecipientsModel(Model): 
    name = Column(String(150), nullable=False)
    emailNotificationRecipientType = Column(String(50), nullable=False)
    emailAddress = Column(String(100), nullable=False)
    notificationFormatType = Column(String(20), nullable=False)
    notificationType = Column(String(20), nullable=False)
    locale = Column(String(10), nullable=False)
    notificationEventType = Column(ARRAY, nullable=False)

    def __repr__(self):
        return self.address
 