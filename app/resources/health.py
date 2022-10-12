
from app.helper.mailer import Mailer
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Resource, Namespace
from smtplib import SMTP 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import os

health_ns = Namespace('health', description='Health check' )
 
mailer = Mailer()
class Health(Resource):
    @health_ns.doc('Get Container health', security = 'apiKey')
    def get(self):
        
        return {'status': 'up'}, 200
 