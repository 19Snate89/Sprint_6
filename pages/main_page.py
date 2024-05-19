import allure
from pages.base_page import BasePage
from locators.main_page_locators import HomePageLocators

class MainPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем главную страницу')
    def open_main_page(self, url):
        self.navigate(url)

    @allure.step('Открываем страницу заказа')
    def open_order_page(self, url):
        self.navigate(f'{url}order')

    @allure.step('Нажимаем на лого Яндекса')
    def click_to_ya_logo(self, locator):
        self.wait_located_elements(locator)
        self.click_element(locator)

    @allure.step('Нажимаем на лого Самокат')
    def click_to_scooter_logo(self, locator):
        self.wait_located_elements(locator)
        self.click_element(locator)

    @allure.step('Проверяем редирект на Дзен в новой вкладке')
    def check_redirect(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.wait_located_element(HomePageLocators.REDIRECT)
            url = self.driver.current_url
        except Exception:
            raise Exception('Что-то пошло не так')
        return url

    @allure.step('Сравниваем ответ в выбранном вопросе')
    def get_answer(self, number):
        method, locator = HomePageLocators.ANSWER
        locator = locator.format(number)
        element = self.find_element((method, locator))
        return element.text

    @allure.step('Открыть пункт Faq')
    def open_faq(self, number):
        method, locator = HomePageLocators.FAQ
        locator = locator.format(number)
        element = self.find_element((method, locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self.click_element((method, locator))
