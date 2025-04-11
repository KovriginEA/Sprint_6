import allure
from pages.order_page import OrderPage
from data import TestData

@allure.suite('Cтраница заказа')
class TestOrderPage:

    @allure.title('Позитивный тест создания заказа через кнопку в хедере')
    def test_create_order_from_button_in_header(self, driver):
        test_data = TestData.test_data_1
        order_page = OrderPage(driver)
        order_page.click_cookie_accept()
        order_page.wait_order_button()
        order_page.click_order_button()
        order_page.fill_first_form(test_data)
        order_page.fill_second_form(test_data)
        assert order_page.check_status_of_order()

    @allure.title('Позитивный тест создания заказа через нижнюю кнопку')
    def test_create_order_from_bottom(self, driver):
        test_data = TestData.test_data_2
        order_page = OrderPage(driver)
        order_page.click_cookie_accept()
        order_page.wait_bottom_order_button()
        order_page.click_bottom_order_button()
        order_page.fill_first_form(test_data)
        order_page.fill_second_form(test_data)
        assert order_page.check_status_of_order()
