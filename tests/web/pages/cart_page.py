import time

import allure
from selene import browser, be, command, have
from tests.web.pages.locators import LocatorsWeb


class CartPage:

    @allure.step("добавление товара в корзину")
    def add_products_to_cart(self):

        button_add_to_cart = browser.all(LocatorsWeb.ADD_TO_CART_BUTTON)

        for button_cart in button_add_to_cart:
            button_cart.click()
            time.sleep(0.5)
            continue_button = browser.element(LocatorsWeb.CONTINUE_BUYING_BUTTON)
            continue_button.should(be.clickable)
            continue_button.perform(command.js.scroll_into_view)
            continue_button.click()

        return self

    @allure.step("проверка счетчика кол-ва продуктов")
    def assert_count_product_to_cart(self):
        cart_count = browser.element(LocatorsWeb.CART_BUTTON).perform(
            command.js.scroll_into_view
        )

        browser.driver.refresh()
        cart_count.should(have.exact_text("КОРЗИНА\n9"))

        return self

    @allure.step('переход в "корзину"')
    def cart_button_click(self):
        browser.element(LocatorsWeb.CART_BUTTON).click()

        return self

    @allure.step("выбор всех товаров")
    def checkbox_select_all_click(self):
        browser.element(LocatorsWeb.SELECT_ALL_PRODUCTS_BUTTON).click()

        return self

    @allure.step("удаление всех товаров")
    def cart_delete_all_button_click(self):
        browser.element(LocatorsWeb.DELETE_ALL_BUTTON).click()

        return self

    @allure.step("проверка, что корзина очищена")
    def assert_text_empty_cart(self, value):
        browser.element(LocatorsWeb.EMPTY_CART_TITLE).should(have.exact_text(value))

        return self
