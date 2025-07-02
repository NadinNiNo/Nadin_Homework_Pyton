from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
import allure


class CheckoutPage(BasePage):
    """Page Object для страницы оформления заказа"""

    FIRST_NAME = ("id", "first-name")
    LAST_NAME = ("id", "last-name")
    ZIP_CODE = ("id", "postal-code")
    CONTINUE_BUTTON = ("id", "continue")
    TOTAL_PRICE = ("class name", "summary_total_label")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Заполнить информацию о доставке")
    def fill_shipping_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        self.find_element(self.FIRST_NAME).send_keys(first_name)
        self.find_element(self.LAST_NAME).send_keys(last_name)
        self.find_element(self.ZIP_CODE).send_keys(zip_code)

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> None:
        self.click_element(self.CONTINUE_BUTTON)

    @allure.step("Получить итоговую стоимость")
    def get_total_price(self) -> str:
        return self.find_element(self.TOTAL_PRICE).text
