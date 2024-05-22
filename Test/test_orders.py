import allure
from pages.oreder_page import OrderPage
from pages.main_page import MainPage
from config import URL


class TestOrder:

    @allure.title('Тест url при переходе на форму заказа по кнопке Заказать')
    def test_url_click_order_button(self, driver):
        op = OrderPage(driver)
        mp = MainPage(driver)
        mp.click_top_order_button()
        url = op.get_url()
        assert f'{URL}order' == url


    @allure.title('Тест заголовка формы заказа')
    def test_url_click_order_button(self, driver):
        op = OrderPage(driver)
        mp = MainPage(driver)
        mp.click_top_order_button()
        op.check_title_order_page('Для кого самокат')

    @allure.title('Тест заполнения данных заказчика по верхней кнопке Заказать')
    def test_top_order_button(self, driver):
        op = OrderPage(driver)
        mp = MainPage(driver)
        mp.click_top_order_button()
        op.enter_name()
        op.enter_surname()
        op.enter_address()
        op.select_metro()
        op.enter_phone()
        op.click_next_button()
        op.check_title_order_page('Про аренду')
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
        mp = MainPage(driver)
        mp.click_bottom_order_button()
        op.enter_name()
        op.enter_surname()
        op.enter_address()
        op.select_metro()
        op.enter_phone()
        op.click_next_button()
        op.check_title_order_page('Про аренду')
        op.enter_date()
        op.click_color()
        op.choose_period()
        op.enter_commentary()
        op.click_order()
        assert "Хотите оформить заказ?" in op.check_text_modal_agreement()
        op.click_yes_button()
        assert "Заказ оформлен" in op.check_successful_modal()


