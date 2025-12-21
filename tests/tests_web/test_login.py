import allure
from tests.web.pages.login_page import LoginPage

login_page = LoginPage()


@allure.epic("авторизация")
@allure.title("сообщение об ошибке при неверном вводе логина и пароля")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login(open_site_without_cookies):

    (
        login_page.go_to_login_page_click()
        .input_login("TestLogin@mail.ru")
        .input_password("TestPassword")
        .login_button_click()
        .assert_login_error_message("Неверный логин или пароль.")
    )
