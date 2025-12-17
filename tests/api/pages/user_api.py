import json
import requests
from jsonschema import validate
from conftest import user_payload
from utils.file import path_from_json_schemas



class User:

    def __init__(self,api_url, headers):
        self.response = None
        self.api_url = api_url
        self.headers = headers

    def post_create_user_request_body(self,user_payload):

        self.response = requests.request(method='POST',
                                url=f'{self.api_url}/v2/user/',
                                headers=self.headers,
                                json=user_payload,
                                timeout=10)


        return self.response


    def validate_post_create_user_response(self):

        with open(path_from_json_schemas("post_create_user.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)


    def get_user_by_username(self,common_username):

        self.response = requests.request(method='GET',
                                    url=f'{self.api_url}/v2/user/{common_username}',
                                    headers=self.headers,
                                    timeout=10
                                    )


        return self.response


