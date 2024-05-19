import datetime
from selenium import webdriver
from locators.main_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def navigate(self, url: str):
        return self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def find_element(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except Exception:
            raise Exception(f'Не удалось найти элемент с локатором {element}')
        return element

    def wait_located_element(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except Exception:
            raise Exception(f'Не удалось найти элемент с локатором {element}')
        return element

    def wait_clickable_element(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        except Exception:
            raise Exception(f'Не удалось найти элемент с локатором {element}')
        return element

    def wait_located_elements(self, locator: tuple):
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        except Exception:
            raise Exception(f'Не удалось найти элементы с локатором {elements}')
        return elements

    def enter_text(self, locator: tuple, text: str):
        element = self.find_element(locator)
        if element:
            element.send_keys(text)
        else:
            print(f'Не удалось найти элемент с локатором: {element}')

    def get_text(self, locator):
        element = self.find_element(locator)
        if element:
            element.text
        else:
            print(f'Не удалось получить текст локатора: {element}')

    def click_element(self, locator: tuple):
        element = self.find_element(locator)
        if element:
            element.click()
        else:
            print(f'Не удалось найти элемент с локатором: {element}')

    def close_cookies(self):
        self.click_element(HomePageLocators.CLOSE_COOKIES)

    def quit_driver(self):
        self.driver.quit()

    def get_date(self):
        get_date = datetime.datetime.now()
        new_date = get_date + datetime.timedelta(days=2)
        date = datetime.datetime.strftime(new_date, '%d.%m.%y')
        return date