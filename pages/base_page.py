from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from locators.main_page_locators import MainPageLocators
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Scroll к элементу')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидаем отображение элемента')
    def wait_visibility_of_element(self, locator):
        return WDW(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    # @allure.step('Ввод значения в поле')
    # def send_keys_to_input(self, locator, keys):
    #     self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Переключаем вкладку')
    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Возвращаем заголовок страницы')
    def get_page_title(self):
        WDW(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.title_of_page))
        return self.driver.title

    @allure.step('Проверка отображения элемента')
    def verify_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()