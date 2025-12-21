import allure
from selene import browser, have

from tests.web.pages.locators import LocatorsWeb


class LoginPage:

    @allure.step("переход на страницу логина")
    def go_to_login_page_click(self):
        browser.element(LocatorsWeb.LOGIN_PAGE_BUTTON).click()
        return self

    @allure.step("ввод логина")
    def input_login(self, value):
        browser.element(LocatorsWeb.INPUT_USER_LOGIN).type(value)

        return self

    @allure.step("ввод пароля")
    def input_password(self, value):
        browser.element(LocatorsWeb.INPUT_USER_PASSWORD).type(value)
        return self

    @allure.step("клик по кнопке логина")
    def login_button_click(self):
        browser.element(LocatorsWeb.LOGIN_BUTTON).click()
        return self

    @allure.step("проверка сообщения об ошибке авторизации")
    def assert_login_error_message(self, value):
        browser.element(LocatorsWeb.LOGIN_ERROR_MESSAGE).should(have.exact_text(value))

        return self
