import allure
from pages.main_page import MainPage
from conftest import driver
from data import TestData
import pytest


class TestMainPageImportantQuestions:
    @allure.title('Проверка раздела вопросов о важном')
    @pytest.mark.parametrize('question_number, answer', TestData.correct_answer)
    def test_click_on_question_display_answer(self, driver, question_number, answer):
        main_page = MainPage(driver)
        main_page.scroll_to_important_question()
        main_page.wait_visibility_question(question_number)
        main_page.click_on_question(question_number)
        main_page.wait_answer_visibility(question_number)
        assert main_page.get_text_of_answer(question_number) == answer