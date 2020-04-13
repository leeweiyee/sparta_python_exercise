import requests
import json

# gucci_request = requests.get("https://www.gucci.com")
# gucci_html = gucci_request.content
#
# if __name__ == '__main__':
#     print(gucci_request.status_code)

postcodes_base_url = "https://api.postcodes.io/"
postcode_endpoint = "postcodes/"
full_postcode_url = postcodes_base_url+postcode_endpoint

def postcode_search_full_response(postcode):
    return requests.get(full_postcode_url+postcode)

def postcode_json_response(postcode):
    return postcode_search_full_response(postcode).json()

def get_status_from_json(postcode):
    return postcode_json_response(postcode)['status']

def get_parish_data_from_code_object(postcode):
    return postcode_json_response(postcode)['result']['codes']

if __name__ == '__main__':
    # print(postcode_search_full_response('se16db').content)
    # print(postcode_search_full_response('se16db').json()) #default
    print(postcode_search_full_response('se16db'))
    print(postcode_json_response('se16db')['status'])
    print(get_status_from_json('se16db'))
    print(get_parish_data_from_code_object('se16db'))
