import imp
from flask import Flask, Blueprint, jsonify
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api
from app.ma import ma
from app.db import db 
from app.resources.health import Health, health_ns  
from app.resources.shippingdata import  shipping_data_ns, ShippingsdataList, Shippingdata, shipping_datas_ns
from marshmallow import ValidationError
from app.config import config_dict
from decouple import config

# # WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

app_config = config_dict[get_config_mode.capitalize()]



app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY', default=None)
app.config['JWT_PRIVATE_KEY'] = config('JWT_PRIVATE_KEY', default=None)
app.config['JWT_PUBLIC_KEY'] = config('JWT_PUBLIC_KEY', default=None)
app.config['JWT_PASE_PHRASE'] = config('JWT_PASE_PHRASE', default=None)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config.from_object(app_config)
bluePrint = Blueprint('api', __name__, url_prefix='/shippingapi')
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api = Api(bluePrint, doc='/doc', title='Deepblu Shpping API', authorizations=authorizations)
app.register_blueprint(bluePrint)


api.add_namespace(health_ns)  
api.add_namespace(shipping_datas_ns)  
api.add_namespace(shipping_data_ns)



@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400



health_ns.add_resource(Health, "") 
shipping_datas_ns.add_resource(ShippingsdataList,"")
shipping_data_ns.add_resource(Shippingdata,"/<int:id>")
db.init_app(app)
ma.init_app(app)