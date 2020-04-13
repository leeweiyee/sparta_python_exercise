from ..http_management import Httpmanager
from ..json_parsing import SinglePostcodeJsonParser

class PostcodesioFactory:

    def __init__(self, postcode):
        self.HTTP_call = Httpmanager.postcode_json_response(postcode)
        self.single_postcode_response = SinglePostcodeJsonParser(self.HTTP_call)

    def single_postcode_data(self):
        return self.single_postcode_response

if __name__ == '__main__':
    print(PostcodesioFactory('se16db').single_postcode_data().get_status_code_from_json)