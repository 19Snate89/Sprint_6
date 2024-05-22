from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, '//button[@class="Button_Button__ra12g"]') # Верхняя кнопка "Заказать" на галавной странице
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//button[contains(@class, "Button_UltraBig__UU3Lp") and text()="Заказать"]') #Нижняя кнопка "Заказать" на галавной странице
    YANDEX_LOGO = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]') # Лого Яндекса
    SCOOTER_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]') # Лого Самокат
    TEXT_HOME_PAGE = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')
    CLOSE_COOKIES = By.ID, "rcc-confirm-button" # Очистка куки
    FAQ = By.XPATH, "//div[@id ='accordion__heading-{}']" # Вопрос
    ANSWER = By.XPATH, "//div[@id='accordion__panel-{}']/p" # Ответ
    REDIRECT = (By.XPATH, "//div[contains(@class, 'floor-title__title-2v') and text()='Новости']")

