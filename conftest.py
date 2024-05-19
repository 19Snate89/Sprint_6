import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome = webdriver.Firefox()
    chrome.maximize_window()
    chrome.get('https://qa-scooter.praktikum-services.ru')
    yield chrome
    chrome.quit()