import json
import requests
from jsonschema import validate
from tests.api.data.generators import payload_generate_user
from utils.file import path_from_json_schemas


class PostCreateUser:


    def __init__(self):
        self.response = None

    def post_request_body(self,api_url,headers,method,endpoint):

        response = requests.request(method=method,
                                url=f'{api_url}{endpoint}',
                                headers=headers,
                                json=payload_generate_user(),
                                timeout=10)


        self.response = response

        return response

    def validate_response_body(self):

        with open(path_from_json_schemas("post_create_user.json"), encoding="utf-8") as file:
            schema = json.load(file)
        validate(self.response.json(), schema)


