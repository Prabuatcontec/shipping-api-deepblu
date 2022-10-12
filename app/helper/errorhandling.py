from sqlalchemy import null
from flask import jsonify, request, session

class Errorhandling(object):
    def error(self, error, req):
        errors = []
        
        for key, value in error.items():
           
            keyVal = None
            for reqkey, reqvalue in req.items():
                if key == reqkey:
                    keyVal = reqvalue
                    break

            valError = ""
            for erkey, ervalue in value.items():
                if valError != "":
                    valError = valError + ', ' + ervalue
                else:
                    valError = ervalue

            er = self.app_property(key, keyVal, key.replace("_", " ").capitalize() +': '+valError)
            
            errors.append(er)
        session.pop('validation', None)
        return self.error_output(errors)
        
    def app_property(self, pro_path, invalid_value, message):
        errors = []
        if isinstance(invalid_value, list):
            invalid_value = session["validation"]
            

        er = {"property_path": pro_path,
            "invalid_value": invalid_value,
            "message": message }
        return er
    
    def error_output(self, errors):
        return {"errors": errors,  'status': 400,
                'title': "Validation error occurred.",
                'type': "validation_error"}

    def app_property_error(self, pro_path, invalid_value, message):
        errors = []
        er = self.app_property(pro_path, invalid_value, message)
        errors.append(er)
        return self.error_output(errors)

    
        

    def password_check(self, passwd):
        specialsym =['$', '@', '#', '%', '!']
        val = True
        error = ""
        errors = []
        if not any(char.isdigit() for char in passwd):
            error = ('Password should have at least one numeral')
            val = False
            
        if not any(char.isupper() for char in passwd):
            error = ('Password should have at least one uppercase letter')
            val = False
            
        if not any(char.islower() for char in passwd):
            error = ('Password should have at least one lowercase letter')
            val = False
            
        if not any(char in specialsym for char in passwd):
            error = ('Password should have at least one of the symbols $@#%!')
            val = False
        
        er = self.app_property("plain_password", passwd, error)
        
        errors.append(er)
        if val == False:
            return self.error_output(errors)
        else:
            return {'status': 200}

            