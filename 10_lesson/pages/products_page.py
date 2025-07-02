import allure
from .base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsPage(BasePage):
    """Класс для страницы продуктов"""

    PRODUCTS_TITLE = ("xpath", "//span[@class='title' and text()='Products']")
    CART_BUTTON = ("class name", "shopping_cart_link")

    @allure.step("Проверить загрузку страницы продуктов")
    def is_page_loaded(self) -> bool:
        """
        Проверить загрузку страницы
        :return: bool - True если страница загружена
        """
        return self.find_element(self.PRODUCTS_TITLE).is_displayed()

    @allure.step("Добавить товар {item_name} в корзину")
    def add_item_to_cart(self, item_name: str) -> None:
        """
        Добавить товар в корзину
        :param item_name: str - название товара
        """
        locator = ("xpath", f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item_description']//button")
        self.click_element(locator)

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Перейти в корзину"""
        self.click_element(self.CART_BUTTON)
