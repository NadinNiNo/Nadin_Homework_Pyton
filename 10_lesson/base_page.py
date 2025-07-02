from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple) -> None:
        self.find_element(locator).click()
 