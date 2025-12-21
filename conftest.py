import allure
import pytest
from faker import Faker
from tests.api.data.generators import payload_generate_user

fake = Faker()

@allure.title('api url')
@pytest.fixture()
def api_url():
    return 'https://petstore.swagger.io'

@allure.title('request headers')
@pytest.fixture()
def headers():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    return headers

@allure.title('генерация payload')
@pytest.fixture(scope="function")
def user_payload():
    return payload_generate_user()

@allure.title('endpoint')
@pytest.fixture()
def common_username(user_payload):
    return user_payload['username']

@pytest.fixture()
def common_password(user_payload):
    return user_payload['password']


