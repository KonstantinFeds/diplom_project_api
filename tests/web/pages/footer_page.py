import allure
from selene import browser, command, be, have

from tests.web.pages.locators import LocatorsWeb


class FooterPage:

    @allure.step('применение немецкого языка в "футере"')
    def select_german_language(self):
        german_button = browser.all(LocatorsWeb.GERMAN_LANGUAGE_BUTTON)
        german_button[1].should(be.visible)
        german_button[1].perform(command.js.scroll_into_view)
        german_button[1].click()

        return self

    @allure.step("перевод категорий на немецкий язык")
    def assert_german_name_catalog(
        self, title1, title2, title3, title4, title5, title6, title7
    ):
        browser.all(LocatorsWeb.ALL_TITLE_NAME_CATALOG).should(
            have.exact_texts(title1, title2, title3, title4, title5, title6, title7)
        )

        return self
