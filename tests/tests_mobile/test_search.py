import allure
from pages.mobile.onboarding_page import OnboardingPage
from pages.mobile.search_page import SearchPage

onboarding_page = OnboardingPage()
search_page = SearchPage()


@allure.epic("поиск")
@allure.title("поиск по заданному тексту")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_by_text():
    onboarding_page.skip_onboarding_button_click()
    (
        search_page.tap_search()
        .insert_text("Gladiator 2000 film")
        .assert_name_result("Gladiator (2000 film)")
    )
