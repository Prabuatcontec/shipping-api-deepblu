import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean , ARRAY
from sqlalchemy.orm import relationship
from flask_appbuilder import Model


class TinsModel(Model):
    streetLines = Column(ARRAY,  nullable=False) 
    def __repr__(self):
        return self.streetLines 
    