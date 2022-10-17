from sqlalchemy import null
import requests


class ShippingdataPaginate(object):
    def paginator(self ,objects, page_no, obj_per_page=20, total_objects=0):
        start = page_no*obj_per_page
        objects = objects[start:start+obj_per_page]
        return {"meta":{"limit":obj_per_page,"page":page_no,"total_items":total_objects,"current_items":len(objects)},"shippping_data":objects}
        

            