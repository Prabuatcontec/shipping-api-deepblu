from array import array
from pydoc import html
from flask import  request, jsonify
import os
import jwt
from smtplib import SMTP 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Mailer(object):
   
    def send_mail(self, 
        subject:str,  
        to_email:array,
        body:html):
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = str(os.getenv('SMTP_USERNAME'))
        message['To'] = to_email

        message.attach(MIMEText(body, "html"))
        msgBody = message.as_string()

        server = SMTP(str(os.getenv('SMTP_HOST')), str(os.getenv('SMTP_PORT')))
        server.starttls()
        server.login(str(os.getenv('SMTP_USERNAME')), str(os.getenv('SMTP_PASSWORD')))
        sent = server.sendmail(str(os.getenv('SMTP_USERNAME')), to_email, msgBody)

        server.quit()
        if sent:
            return True
        else:
            return False