import pytest
from selenium import webdriver
import allure


@pytest.fixture
def browser():
    with allure.step("Initialize browser"):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver

    with allure.step("Close browser"):
        driver.quit()
