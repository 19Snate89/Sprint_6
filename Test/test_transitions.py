import allure
from locators.main_page_locators import HomePageLocators
from pages.main_page import MainPage
from config import URL, URL_REDIRECT


class TestTransition:

    @allure.title('Проверка редиректа по лого Яндекса')
    def test_url_click_order_button(self, driver):
        mp = MainPage(driver)
        mp.open_main_page(URL)
        mp.click_to_ya_logo()
        url = mp.check_redirect()
        assert URL_REDIRECT == url

    @allure.title('Проверка URL по лого Самоката')
    def test_transition_scooter_page(self, driver):
        mp = MainPage(driver)
        mp.click_to_scooter_logo()
        assert URL == mp.get_url()