import json
class Shippingmodel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if type(v) is dict:
                setattr(self, k, Shippingmodel(**v))
            else:
                setattr(self, k, v)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
 