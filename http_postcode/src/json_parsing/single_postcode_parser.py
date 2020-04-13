class SinglePostcodeJsonParser:

    def __init__(self, json):
        self.json = json

    def get_status_code_from_json(self):
        return self.json['status']

    def get_parish_data_from_code_object(self):
        return self.json['result']['code']['parish']