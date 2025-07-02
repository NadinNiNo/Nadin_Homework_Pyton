from .base_page import BasePage
import allure


class CartPage(BasePage):
    CHECKOUT_BUTTON = ("id", "checkout")
    ITEM_NAMES = ("class name", "inventory_item_name")

    @allure.step("Get cart items")
    def get_cart_items(self) -> list[str]:
        return [item.text for item in self.find_elements(self.ITEM_NAMES)]

    @allure.step("Click checkout")
    def click_checkout(self) -> None:
        self.click_element(self.CHECKOUT_BUTTON)

