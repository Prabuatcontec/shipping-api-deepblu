import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY, Float
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class TotalDeclaredValueModel(Model):
    amount = Column(Float(precision=None, asdecimal=False, decimal_return_scale=2),  nullable=False)
    currency = Column(String(5), nullable=False) 

    def __repr__(self):
        return self.amount 