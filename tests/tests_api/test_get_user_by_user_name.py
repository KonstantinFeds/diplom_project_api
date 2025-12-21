import allure

from tests.api.pages.user_api import User

@allure.epic('получение пользователя')
@allure.title('успешное получение пользователя')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user_by_user_name_success(api_url,headers,user_payload,common_username):
    user = User(api_url, headers)


    user.post_create_user_request_body(user_payload)

    get_response = user.get_user_by_username(common_username)

    assert get_response.status_code == 200
    user.validate_get_user_response()
    user.assert_get_response_body(user_payload)

    user.delete_user(common_username)


