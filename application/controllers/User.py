import json

import requests


class User:
    def __init__(self):
        pass

    @classmethod
    def get_user_details(cls, phone_number="9886622444", location="BNG"):
        payload = {"source": "Saturam", "mobileNumber": phone_number, "locationCode": location}
        url = "https://lmrapi1.landmarkrewards.in:7002/CustStoreExpAppWS/CustStoreExpService/StoreCustomerDetails"

        headers = {
            "Accept": "application/json",
            "AuthKey": "6OJ5UM7DE7P7QR33NFGJ8G1E5AII9L65CGNVPO3CUG7GQD31JR",
            "Content-Type": "application/json"
        }
        _response = requests.post(url, data=json.dumps(payload), headers=headers)
        return _response.json()

