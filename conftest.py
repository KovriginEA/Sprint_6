import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@allure.title("Подготовка драйвера")
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()
