from selenium.webdriver.common.by import By

class ClientOrder:
    ORDER_HEADER = (By.XPATH, '//div[@class="Order_Header__BZXOb"]') # Заголовок формв заказа
    NAME_FIELD = (By.XPATH, '//*[@placeholder="* Имя"]') # Поле Имя
    SURNAME_FIELD = (By.XPATH, '//*[@placeholder="* Фамилия"]') # Поле Фамилия
    ADDRESS_FIELD = (By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]') # Поле Адрес
    METRO_FIELD = (By.XPATH, '//*[@placeholder="* Станция метро"]')
    METRO_STATION = (By.XPATH, ".//button[@value='58']")# Выпадающий список станций метро
    PHONE_FIELD = (By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]') # Поле Адрес
    DATE_PICKER_FIELD = (By.XPATH, '//*[@placeholder="* Когда привезти самокат"]')  # Поле Имя
    PERIOD_AREND_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    PERIOD_AREND_2_DAYS = (By.XPATH, "//div[text()='двое суток']")
    BLACK_COLOR_SCOOTER_CHECKBOX = (By.XPATH, '//*[@id="black"]')
    GREY_COLOR_SCOOTER_CHECKBOX = (By.XPATH, '//*[@id="grey"]')
    COMMENTARY_FIELD = (By.XPATH, '//*[@placeholder="Комментарий для курьера"]')
    AGREEMENT_MODAL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Хотите оформить заказ?']")
    SUCCESS_MODAL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    BACK_BUTTON = (By.XPATH, '//button[text()="Назад"]')
    YES_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text()="Да"]')
    ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')
    STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

