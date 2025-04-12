import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Ждем прогрузку кнопки заказать')
    def wait_order_button(self):
        self.wait_visibility_of_element(MainPageLocators.order_button)

    @allure.step('Клик по кнопке заказать')
    def click_order_button(self):
        self.click_on_element(MainPageLocators.order_button)

    @allure.step('Ждем прогрузку логотипа самокат')
    def wait_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.logo_scooter)

    @allure.step('Ждем загрузку лого яндекс')
    def wait_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.logo_yandex)

    @allure.step('Кликнуть по надписи самокат')
    def click_logo_scooter(self):
        self.click_on_element(MainPageLocators.logo_scooter)

    @allure.step('Клик по надписи яндекс')
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.logo_yandex)

    @allure.step('Подождать прогрузки отображения заголовка главной страницы')
    def wait_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Проверить отображение заголовка главной страницы')
    def verify_main_header_is_displaying(self):
        return self.verify_displaying_of_element(MainPageLocators.main_header)

    @allure.step('Скролл на секцию вопросов  о важном')
    def scroll_to_important_question(self):
        self.scroll_to_element(MainPageLocators.question_section)

    @allure.step('Ожидание загрузки вопроса')
    def wait_visibility_question(self, data):
        self.wait_visibility_of_element(MainPageLocators.questions[data])

    @allure.step('Клик на вопрос')
    def click_on_question(self, data):
        self.click_on_element(MainPageLocators.questions[data])

    @allure.step('Ожидание загрузки ответа')
    def wait_answer_visibility(self, data):
        self.wait_visibility_of_element(MainPageLocators.answers[data])

    @allure.step('Получение текста ответа')
    def get_text_of_answer(self, data):
        return self.get_text(MainPageLocators.answers[data])