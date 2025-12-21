import allure
from tests.mobile.pages.onboarding_page import OnboardingPage

onboarding_page = OnboardingPage()


@allure.epic("онбординг")
@allure.title("настройка языка")
@allure.severity(allure.severity_level.NORMAL)
def test_add_language():

    (
        onboarding_page.add_or_edit_languages_button_click()
        .add_language_button_click()
        .open_search_tap()
        .insert_language_in_search("Russian")
        .result_click()
        .back_button_click()
        .assert_available_language("Русский")
    )
