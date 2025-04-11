from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_button = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
    input_name = (By.XPATH, "//input[@placeholder='* Имя']")
    input_lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    input_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    input_metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    select_metro = (By.XPATH, ".//li[@class='select-search__row']")
    input_phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, "//button[text()='Далее']")
    button_cookie = (By.XPATH, '//button[@id="rcc-confirm-button" and contains(@class, "App_CookieButton")]')

    input_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    grey_scooter = (By.XPATH, "//input[@id='grey']")
    rent_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    choose_rent_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='двое суток']")
    input_comments = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    button_made_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    button_yes_in_confirm = (By.XPATH, "//button[text()='Да']")
    button_status_of_order = (By.XPATH, ".//*[text()='Посмотреть статус']")
    order_button_bottom = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')