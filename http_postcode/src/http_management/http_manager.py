import requests

class Httpmanager:

    def __init__(self):
        self.postcodes_base_url = "https://api.postcodes.io/"
        self.postcode_endpoint = "postcodes/"
        self.full_postcodes_url = self.postcodes_base_url + self.postcode_endpoint

    def postcode_search_full_response(self, postcode):
        return requests.get(self.full_postcodes_url + postcode)

    def postcode_json_response(self, postcode):
        return self.postcode_search_full_response(postcode).json()