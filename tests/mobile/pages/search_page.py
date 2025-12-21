import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from tests.mobile.pages.locators import LocatorsMob


class SearchPage:

    @allure.step("tap по строке поиска")
    def tap_search(self):
        browser.element((AppiumBy.ID, LocatorsMob.OPEN_SEARCH_BUTTON)).click()

        return self

    @allure.step("ввод текста в строку поиска")
    def insert_text(self, value):
        browser.element((AppiumBy.ID, LocatorsMob.SEARCH_TEXT_INPUT)).type(value)

        return self

    @allure.step("выдача результатов по заданному тексту")
    def assert_name_result(self, value):
        browser.element((AppiumBy.ID, LocatorsMob.RESULT_LIST)).should(
            have.exact_text(value)
        )

        return self
