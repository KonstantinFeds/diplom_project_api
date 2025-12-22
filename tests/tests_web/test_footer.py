import allure
from pages.web.footer_page import FooterPage

footer_page = FooterPage()


@allure.epic("footer сайта")
@allure.title("переключение языка на сайта")
@allure.severity(allure.severity_level.MINOR)
def test_switch_to_german_language(open_site_without_cookies):
    (
        footer_page.select_german_language().assert_german_name_catalog(
            "Kopf -\nGerät",
            "Die akustischen\nSysteme",
            "Ein lautes\nGeräusch",
            "Subwoofer",
            "Verstärker",
            "Kopfhörer",
            "Tragbare\nAkustik",
        )
    )
