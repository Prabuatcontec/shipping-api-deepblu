import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY, Float
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class AccountNumberModel(Model): 
    value = Column(String(50), nullable=False) 

    def __repr__(self):
        return self.amount 