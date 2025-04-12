import pytest
import allure
from selenium import webdriver

@allure.title("Подготовка драйвера")
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()
