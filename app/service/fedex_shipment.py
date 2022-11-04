import json
import os
import requests


class FedexshipmentService(object):
    def get_token(self):
        try:
            grant_type = "client_credentials"
            client_id = os.getenv("FEDEX_CLIENT_ID")
            client_secret = os.getenv("FEDEX_CLIENT_SECRET")

            auth_token_url = os.getenv("FEDEX_AUTH_TOKEN_URL")
            payload = {'grant_type': grant_type,
                       'client_id': client_id,
                       'client_secret': client_secret}
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"
            }

            response = requests.request(
                "POST", auth_token_url, data=payload, headers=headers)
            if response.status_code == 200:
                return json.loads(response.text)

            return False
        except Exception as e:
            print(e)
            return False

    def shipment(self, shipment):
        auth_token_url = os.getenv("FEDEX_SHIPMENT_URL") 
        headers = {
            'Content-Type': "application/json",
            'X-locale': "en_US",
            'Authorization': "Bearer "
        }
        payload = shipment['fedex_shipment']
        response = requests.request(
            "POST", auth_token_url, data=payload, headers=headers)
        if response.status_code == 200:
            output = json.loads(response.text)
            return json.loads(response.text)
        return False
