from array import array
from datetime import datetime 
from flask import jsonify, request, session
class Shippingvalidater(object):
    def rule(self):
        rule = { 
        "data":  self.func_shipping_data }
        return rule

        
    def func_shipping_data(self, items):

        ret = True
        print(items)
        if isinstance(items, dict):
            result = {}
            result["data"] = {}
            l = 0
            for item in items:
                result["data"][l] = {}
                if 'alt_name' in item:
                    if not isinstance(item['id'], str): 
                        result["data"][l]["alt_name"]  = "Alt Name must be string"
                        ret = False
                else:
                        result["data"][l]["alt_name"]  = "Alt Name is required"
                        ret = False

                if 'label' in item:
                    if not isinstance(item['label'], str): 
                        result["data"][l]["label"]  = "Label must be string"
                        ret = False 
                else:
                        result["data"][l]["label"]  = "Label Name is required"
                        ret = False

                if 'device_type' in item:
                    if not isinstance(item['device_type'], str): 
                        result["data"][l]["device_type"]  = "Device Type must be string"
                        ret = False 
                else:
                        result["data"][l]["device_type"]  = "Device Type is required"
                        ret = False
                
                if 'order_line_id' in item:
                    if not isinstance(item['order_line_id'], int): 
                        result["data"][l]["order_line_id"]  = "Order Line Id must be integer"
                        ret = False 
                else:
                        result["data"][l]["order_line_id"]  = "Order Line Id is required"
                        ret = False
                
                if 'ship_line_id' in item:
                    if not isinstance(item['ship_line_id'], int): 
                        result["data"][l]["ship_line_id"]  = "Ship Line Id must be integer"
                        ret = False 
                else:
                        result["data"][l]["ship_line_id"]  = "Ship Line Id is required"
                        ret = False
                
                if 'add_user' in item:
                    if not isinstance(item['add_user'], str): 
                        result["data"][l]["add_user"]  = "Add User must be string"
                        ret = False 
                else:
                        result["data"][l]["add_user"]  = "Add User is required"
                        ret = False
                
                if 'ship_id' in item:
                    if not isinstance(item['ship_id'], str): 
                        result["data"][l]["ship_id"]  = "Ship Id must be string"
                        ret = False 
                else:
                        result["data"][l]["ship_id"]  = "Ship Id is required"
                        ret = False
                
                if 'order_id' in item:
                    if not isinstance(item['order_id'], str): 
                        result["data"][l]["order_id"]  = "Order Id must be string"
                        ret = False 
                else:
                        result["data"][l]["order_id"]  = "Order Id is required"
                        ret = False
                if len(result["data"][l]) == 0:
                    del result["data"][l]
                l = l + 1

                        

            if result:
                session["validation"] = result
             
            return ret
        else:
            return False

    def func_bool(self,x):
        if x == True:
            return True
        elif x == False:
            return True
        else:
            return False
    
    def func_float(self,x):
        if isinstance(x, float):
            return True
        else:
            if isinstance(x, int):
                return True
            else:
                return False

            

    def date_time_validator(self, time):
        timeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
        try:
            validtime = datetime.strptime(time, timeformat)
            return True
        except ValueError:
            return False
 
    def date_time_validator_no_zone(self, time):
        timeformat = '%Y-%m-%d %H:%M:%S'
        try:
            validtime = datetime.strptime(time, timeformat)
            return True
        except ValueError:
            return False
 