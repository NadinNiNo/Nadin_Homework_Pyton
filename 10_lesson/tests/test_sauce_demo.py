import allure
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка итоговой стоимости заказа")
def test_checkout_total_price(browser):
    # Тест остается без изменений
    ...
