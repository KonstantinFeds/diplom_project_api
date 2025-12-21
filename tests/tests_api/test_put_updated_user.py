import allure
from tests.api.pages.user_api import User


@allure.epic('обновление пользователя')
@allure.title('успешное обновление пользователя')
@allure.severity(allure.severity_level.CRITICAL)
def test_put_update_user_success(api_url,headers,user_payload,common_username):

    user = User(api_url, headers)


    user.post_create_user_request_body(user_payload)

    user.generate_update_payload(user_payload)

    user.validate_put_user_payload(user.update_payload)

    response_put = user.put_update_user_request_body(common_username, user.update_payload)

    assert response_put.status_code == 200

    user.validate_put_user_response()

    user.assert_user_updated_successfully(user_payload, user.update_payload)

    user.delete_user(user.new_username)




