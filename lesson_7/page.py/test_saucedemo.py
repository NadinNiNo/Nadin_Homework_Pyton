import pytest
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_complete_purchase(browser):
    # 1. Open site and login
    browser.get("https://www.saucedemo.com/")
    login_page = LoginPage(browser)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 2. Add items to cart
    products_page = ProductsPage(browser)
    products_page.add_item_to_cart("backpack")
    products_page.add_item_to_cart("bolt-t-shirt")
    products_page.add_item_to_cart("onesie")
    products_page.go_to_cart()

    # 3. Proceed to checkout
    cart_page = CartPage(browser)
    cart_page.click_checkout()

    # 4. Fill info and check total
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_shipping_info("John", "Doe", "12345")
    total_amount = checkout_page.get_total_amount()
    
    assert total_amount == "58.29", f"Expected $58.29, but got ${total_amount}"
