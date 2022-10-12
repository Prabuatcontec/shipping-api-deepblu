from app.ma import ma
from app.models.shippings import InvoicesModel
from app.db import db 


class shippingSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = InvoicesModel 
        load_instance = True
        include_relationships  = True
        sqla_session = db.session 
    
