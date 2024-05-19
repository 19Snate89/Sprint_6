import allure
from locators.main_page_locators import HomePageLocators
from locators.order_page_locators import ClientOrder
from pages.oreder_page import OrderPage
from config import URL




class TestOrder:

    @allure.title('Тест url при переходе на форму заказа по кнопке Заказать')
    def test_url_click_order_button(self, driver):
        op = OrderPage(driver)
        op.navigate(URL)
        op.wait_located_element(HomePageLocators.ORDER_BUTTON_TOP)
        op.click_element(HomePageLocators.ORDER_BUTTON_TOP)
        url = op.get_url()
        assert f'{URL}order' == url


    @allure.title('Тест заголовка формы заказа')
    def test_url_click_order_button(self, driver):
        op = OrderPage(driver)
        op.click_top_order_button()
        title = op.find_element(ClientOrder.ORDER_HEADER).text
        assert 'Для кого самокат' in title

    @allure.title('Тест заполнения данных заказчика по верхней кнопке Заказать')
    def test_top_order_button(self, driver):
        op = OrderPage(driver)
        op.click_top_order_button()
        op.enter_name()
        op.enter_surname()
        op.enter_address()
        op.select_metro()
        op.enter_phone()
        op.click_next_button()
        title = op.find_element(ClientOrder.ORDER_HEADER).text
        assert title == 'Про аренду'
        op.enter_date()
        op.click_color()
        op.choose_period()
        op.enter_commentary()
        op.click_order()
        assert "Хотите оформить заказ?" in op.check_text_modal_agreement()
        op.click_yes_button()
        assert "Заказ оформлен" in op.check_successful_modal()

    @allure.title('Тест заполнения данных заказчика по нижней кнопке Заказать')
    def test_bottom_order_button(self, driver):
        op = OrderPage(driver)
        op.click_bottom_order_button()
        op.enter_name()
        op.enter_surname()
        op.enter_address()
        op.select_metro()
        op.enter_phone()
        op.click_next_button()
        title = op.find_element(ClientOrder.ORDER_HEADER).text
        assert title == 'Про аренду'
        op.enter_date()
        op.click_color()
        op.choose_period()
        op.enter_commentary()
        op.click_order()
        assert "Хотите оформить заказ?" in op.check_text_modal_agreement()
        op.click_yes_button()
        assert "Заказ оформлен" in op.check_successful_modal()


