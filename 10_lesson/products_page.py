from .base_page import BasePage
import allure


class ProductsPage(BasePage):
    PRODUCTS_TITLE = ("xpath", "//span[@class='title' and text()='Products']")
    CART_BUTTON = ("class name", "shopping_cart_link")

    @allure.step("Verify products page loaded")
    def is_page_loaded(self) -> bool:
        return self.find_element(self.PRODUCTS_TITLE).is_displayed()

    @allure.step("Add item {item_name} to cart")
    def add_item_to_cart(self, item_name: str) -> None:
        xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item_description']//button"
        self.click_element(("xpath", xpath))

    @allure.step("Go to cart")
    def go_to_cart(self) -> None:
        self.click_element(self.CART_BUTTON)
