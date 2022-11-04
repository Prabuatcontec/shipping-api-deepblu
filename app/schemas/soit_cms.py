from app.ma import ma
from app.models.sdct import SdctModel 
from app.db import db 


class SoitcmsSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = SdctModel 
        load_instance = True
        include_relationships  = True
        sqla_session = db.session 
    
