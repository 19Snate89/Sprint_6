import allure

from locators.order_page_locators import ClientOrder
from locators.main_page_locators import HomePageLocators
from pages.base_page import BasePage
from config import CLIENT_DATA


class OrderPage(BasePage):

    @allure.step('Заполнить поле Имя')
    def enter_name(self):
        self.enter_text(ClientOrder.NAME_FIELD, CLIENT_DATA['name'])

    @allure.step('Заполнить поле Фамилия')
    def enter_surname(self):
        self.enter_text(ClientOrder.SURNAME_FIELD, CLIENT_DATA['surname'])

    @allure.step('Заполнить поле Адрес')
    def enter_address(self):
        self.enter_text(ClientOrder.ADDRESS_FIELD, CLIENT_DATA['address'])

    @allure.step('Заполнить поле Станция метро')
    def select_metro(self):
        self.enter_text(ClientOrder.METRO_FIELD, CLIENT_DATA['station'])
        self.click_element(ClientOrder.METRO_STATION)

    @allure.step('Заполнить поле Телефон')
    def enter_phone(self):
        self.enter_text(ClientOrder.PHONE_FIELD, CLIENT_DATA['phone'])

    @allure.step('Клик по кнопке Далее')
    def click_next_button(self):
        self.click_element(ClientOrder.NEXT_BUTTON)

    @allure.step('Клик по кнопке верехней кнопке Заказать')
    def click_top_order_button(self):
        self.click_element(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step('Клик по кнопке нижней кнопке Заказать')
    def click_bottom_order_button(self):
        element = self.find_element(HomePageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.click_element(HomePageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Заполнить поле Комментарий для курьера')
    def enter_commentary(self):
        self.enter_text(ClientOrder.COMMENTARY_FIELD, CLIENT_DATA['commentary'])

    @allure.step('Выбрать цвет самоката')
    def click_color(self):
        self.click_element(ClientOrder.BLACK_COLOR_SCOOTER_CHECKBOX)

    @allure.step('Клик по кнопке Да')
    def click_yes_button(self):
        self.click_element(ClientOrder.YES_BUTTON)

    @allure.step('Выбрать период')
    def choose_period(self):
        self.click_element(ClientOrder.PERIOD_AREND_FIELD)
        self.click_element(ClientOrder.PERIOD_AREND_2_DAYS)

    @allure.step('Клик по кнопке заказать')
    def click_order(self):
        self.click_element(ClientOrder.ORDER_BUTTON)

    @allure.step('Заполнить дату заказа')
    def enter_date(self):
        self.click_element(ClientOrder.DATE_PICKER_FIELD)
        self.enter_text(ClientOrder.DATE_PICKER_FIELD, self.get_date())

    @allure.step('Получить текст Заказ оформлен в окошке с номером заказа')
    def order_successfully(self):
        return self.get_text(ClientOrder.SUCCESS_MODAL)

    def check_text_modal_agreement(self):
        modal = self.wait_located_element(ClientOrder.AGREEMENT_MODAL)
        return modal.text

    def check_successful_modal(self):
        modal = self.wait_located_element(ClientOrder.SUCCESS_MODAL)
        return modal.text


