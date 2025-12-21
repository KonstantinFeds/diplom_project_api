import allure
from tests.web.pages.catalog_page import CatalogPage

catalog_page = CatalogPage()


@allure.epic("фильтры")
@allure.title('применение фильтра "АК" и "Булава" в каталоге')
@allure.severity(allure.severity_level.NORMAL)
def test_series_filter_works_in_subwoofers_catalog(open_site_without_cookies):

    (
        catalog_page.go_to_the_catalog_subwoofer()
        .checkbox_filter_series_ak_click()
        .checkbox_filter_series_bulava_click()
        .assert_products_with_filter(
            "СЕРИЯ БУЛАВА", "СЕРИЯ АК", "СЕРИЯ АК", "СЕРИЯ БУЛАВА", "СЕРИЯ БУЛАВА"
        )
    )
