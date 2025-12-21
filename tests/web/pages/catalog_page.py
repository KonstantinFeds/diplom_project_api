import allure
from selene import browser, have
from tests.web.pages.locators import LocatorsWeb


class CatalogPage:

    @allure.step('переход в каталог "Cабвуферы"')
    def go_to_the_catalog_subwoofer(self):
        browser.element(LocatorsWeb.CATALOG_BUTTON).click()
        browser.element(LocatorsWeb.CATALOG_SUBWOOFERS_BUTTON).click()

        return self

    @allure.step('проверка наименования каталога "Cабвуферы"')
    def assert_name_catalog_subwoofer(self, value):
        browser.element(LocatorsWeb.TITLE_CATALOG_SUBWOOFERS).should(
            have.exact_text(value)
        )

        return self

    @allure.step('переход в каталог "Акустика"')
    def go_to_the_catalog_dinamiki(self):
        browser.element(LocatorsWeb.CATALOG_BUTTON).click()
        browser.element(LocatorsWeb.CATALOG_DINAMIKI_BUTTON).click()

        return self

    @allure.step("проверка наличия товаров в каталоге")
    def assert_products_in_the_catalog(
        self,
        product1,
        product2,
        product3,
        product4,
        product5,
        product6,
        product7,
        product8,
        product9,
    ):
        (
            browser.all(LocatorsWeb.ALL_PRODUCTS_CATALOG).should(
                have.exact_texts(
                    product1,
                    product2,
                    product3,
                    product4,
                    product5,
                    product6,
                    product7,
                    product8,
                    product9,
                )
            )
        )

        return self

    @allure.step('выбор фильтра "АК"')
    def checkbox_filter_series_ak_click(self):
        browser.element(LocatorsWeb.CHECKBOX_SERIES_NAME_AK).click()
        return self

    @allure.step('выбор фильтра "Булава"')
    def checkbox_filter_series_bulava_click(self):
        browser.element(LocatorsWeb.CHECKBOX_SERIES_NAME_BULAVA).click()
        return self

    @allure.step("проверка товаров после применения фильтра")
    def assert_products_with_filter(
        self, product1, product2, product3, product4, product5
    ):
        browser.all(LocatorsWeb.CATALOG_RESULTS_PRODUCTS).should(
            have.exact_texts(product1, product2, product3, product4, product5)
        )

        return self
