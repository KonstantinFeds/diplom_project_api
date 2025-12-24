import allure
import pytest
from faker import Faker
import config
from data.generators import payload_generate_user

fake = Faker()


@pytest.fixture(scope="session", autouse=True)
def clean_allure_results():
    config.clear_allure_results()


@allure.title("api url")
@pytest.fixture()
def api_url():
    return "https://petstore.swagger.io"


@allure.title("request headers")
@pytest.fixture()
def headers():
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    return headers


@allure.title("генерация payload")
@pytest.fixture(scope="function")
def user_payload():
    return payload_generate_user()


@allure.title("username")
@pytest.fixture()
def common_username(user_payload):
    return user_payload["username"]


@allure.title("password")
@pytest.fixture()
def common_password(user_payload):
    return user_payload["password"]
