import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Подождать прогрузки кнопки "Заказать" в хэдере')
    def wait_order_button(self):
        self.wait_visibility_of_element(MainPageLocators.order_button)

    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_order_button(self):
        self.click_on_element(MainPageLocators.order_button)

    @allure.step('Подождать прогрузки части лого с надписью "Самокат" в хэдере')
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

    # @allure.step('Проскроллить до секции "Вопросы о важном"')
    # def scroll_to_faq_section(self):
    #     self.scroll_to_element(MainPageLocators.faq_section)
    #
    # @allure.step('Подождать прогрузки нужного номера вопроса в аккордеоне "Вопросы о важнoм"')
    # def wait_visibility_of_faq_items(self, data):
    #     self.wait_visibility_of_element(MainPageLocators.faq_questions_items[data])
    #
    # @allure.step('Кликнуть на нужный номер вопроса в аккордеоне "Вопросы о важнoм"')
    # def click_on_faq_items(self, data):
    #     self.click_on_element(MainPageLocators.faq_questions_items[data])
    #
    # @allure.step('Подождать прогрузки нужного номера ответа в аккордеоне "Вопросы о важнoм"')
    # def wait_visibility_of_faq_answer(self, data):
    #     self.wait_visibility_of_element(MainPageLocators.faq_answers_items[data])
    #
    # @allure.step('Получить текст нужного номера ответа в аккордеоне "Вопросы о важнoм"')
    # def get_displayed_text_from_faq_answer(self, data):
    #     return self.get_text_on_element(MainPageLocators.faq_answers_items[data])