import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from app.models.fedex.payor import PayorModel 
from flask_appbuilder import Model





class ShippingChargesPaymentModel(Model):
    payor = relationship("PayorModel") 
    paymentType = Column(String(150), nullable=False)

    def __repr__(self):
        return self.address
 