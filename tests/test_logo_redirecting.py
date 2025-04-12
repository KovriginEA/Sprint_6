import allure
from conftest import driver
from pages.main_page import MainPage


class TestLogoRedirect:
    @allure.title('Проверка перехода, при клике на логотип самоката, на главную страницу')
    def test_click_on_scooter_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_order_button()
        main_page.click_order_button()
        main_page.wait_logo_scooter()
        main_page.click_logo_scooter()
        main_page.wait_main_header()
        assert main_page.verify_main_header_is_displaying()

    @allure.title('Проверка перехода, при клике на логотип яндекс, на страницу дзена')
    def test_click_on_yandex_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_logo_yandex()
        main_page.click_logo_yandex()
        main_page.switch_tab()
        assert 'Дзен' in main_page.get_page_title()