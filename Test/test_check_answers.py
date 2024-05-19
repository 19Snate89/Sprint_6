import allure
import pytest

from conftest import driver
from pages.main_page import MainPage
from config import ANSWERS


class TestCheckAnswer:
    @allure.title('Проверка блока "Вопросы о важном"')
    @pytest.mark.parametrize('num, exp_answer', ANSWERS)
    def test_faq(self, driver, num, exp_answer):
        mp = MainPage(driver)
        mp.close_cookies()
        mp.open_faq(num)
        answer = mp.get_answer(num)
        assert answer == exp_answer
