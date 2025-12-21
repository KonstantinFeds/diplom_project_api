import allure
from tests.mobile.pages.login_page import LoginPage
from tests.mobile.pages.onboarding_page import OnboardingPage

onboarding_page = OnboardingPage()
login_page = LoginPage()


@allure.epic("авторизация")
@allure.title("авторизация при неверном логине и пароле")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login():

    onboarding_page.skip_onboarding_button_click()
    (
        login_page.more_menu_click()
        .go_to_create_account_page()
        .go_to_login_page()
        .username_tap()
        .insert_username("Test@gmail.com")
        .password_tap()
        .insert_password("test1122")
        .login_button_click()
        .assert_error_msg_login("Invalid characters in username")
    )
