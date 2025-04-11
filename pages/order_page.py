import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import TestData


class OrderPage(BasePage):

    @allure.step('Ждем прогрузку кнопки заказать')
    def wait_order_button(self):
        self.wait_visibility_of_element(OrderPageLocators.order_button)

    @allure.step('Ждем прогрузку нижней кнопки заказать')
    def wait_bottom_order_button(self):
        self.wait_visibility_of_element(OrderPageLocators.order_button_bottom)

    @allure.step('Клик по нижней кнопке заказать')
    def click_bottom_order_button(self):
        self.click_on_element(OrderPageLocators.order_button_bottom)


    @allure.step('Клик по кнопке заказать')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.order_button)

    @allure.step('Клик принять куки')
    def click_cookie_accept(self):
        self.click_on_element(OrderPageLocators.button_cookie)


    @allure.step('Заполнение первой формы')
    def fill_first_form(self, test_data):

        # self.click_on_element(OrderPageLocators.button_cookie)
        self.wait_visibility_of_element(OrderPageLocators.input_name)
        self.click_on_element(OrderPageLocators.input_name)
        self.send_value_to_input(OrderPageLocators.input_name, test_data[0])
        self.click_on_element(OrderPageLocators.input_lastname)
        self.send_value_to_input(OrderPageLocators.input_lastname, test_data[1])
        self.click_on_element(OrderPageLocators.input_address)
        self.send_value_to_input(OrderPageLocators.input_address, test_data[2])
        self.click_on_element(OrderPageLocators.input_metro)
        self.send_value_to_input(OrderPageLocators.input_metro, test_data[3])
        self.click_on_element(OrderPageLocators.select_metro)
        self.click_on_element(OrderPageLocators.input_phone)
        self.send_value_to_input(OrderPageLocators.input_phone, test_data[4])
        self.scroll_to_element(OrderPageLocators.button_next)
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Заполнение второй формы')
    def fill_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.input_date)
        self.click_on_element(OrderPageLocators.input_date)
        self.send_value_to_input(OrderPageLocators.input_date, test_data[5])
        self.click_on_element(OrderPageLocators.grey_scooter)
        self.click_on_element(OrderPageLocators.rent_period)
        self.click_on_element(OrderPageLocators.choose_rent_period)
        self.click_on_element(OrderPageLocators.input_comments)
        self.send_value_to_input(OrderPageLocators.input_comments, test_data[6])
        self.click_on_element(OrderPageLocators.button_made_order)
        self.wait_visibility_of_element(OrderPageLocators.button_yes_in_confirm)
        self.click_on_element(OrderPageLocators.button_yes_in_confirm)

    @allure.step('Проверка появление кнопки посмотреть статус')
    def check_status_of_order(self):
        return self.verify_displaying_of_element(OrderPageLocators.button_status_of_order)