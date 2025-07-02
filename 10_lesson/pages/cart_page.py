import allure
from .base_page import BasePage


class CartPage(BasePage):
    """Класс для страницы корзины"""

    CART_ITEMS = ("class name", "cart_item")
    CHECKOUT_BUTTON = ("id", "checkout")
    ITEM_NAMES = ("class name", "inventory_item_name")

    @allure.step("Проверить наличие товаров в корзине")
    def get_cart_items(self) -> list[str]:
        """Получить список товаров в корзине"""
        return [item.text for item in self.find_elements(self.ITEM_NAMES)]

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """Нажать кнопку оформления заказа"""
        self.click_element(self.CHECKOUT_BUTTON)
