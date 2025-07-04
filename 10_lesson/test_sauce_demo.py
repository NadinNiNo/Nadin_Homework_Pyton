import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@allure.feature("Процесс оформления заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка расчета итоговой стоимости")
def test_checkout_total_price():
    # Настройка опций Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Инициализация драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 1. Авторизация на сайте
        with allure.step("1. Авторизация"):
            driver.get("https://www.saucedemo.com/")

            # Ожидаем появление поля логина и вводим данные
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

            # Вводим пароль
            driver.find_element(By.ID, "password").send_keys("secret_sauce")

            # Кликаем кнопку входа
            driver.find_element(By.ID, "login-button").click()

            # Ждем перехода на страницу товаров
            WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

        # 2. Добавление товаров в корзину
        with allure.step("2. Добавление товаров в корзину"):
            # Список товаров для добавления
            items = [
                "Sauce Labs Backpack", 
                "Sauce Labs Bolt T-Shirt", 
                "Sauce Labs Onesie"
            ]

            for item in items:
                # Формируем XPath для кнопки "Add to cart" конкретного товара
                xpath = f"//div[text()='{item}']/ancestor::div[@class='inventory_item_description']//button"

                # Ожидаем пока кнопка станет кликабельной и кликаем
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))).click()

                # Небольшая пауза между добавлениями товаров
                time.sleep(0.3)

        # 3. Переход в корзину
        with allure.step("3. Переход в корзину"):
            # Ожидаем и кликаем на иконку корзины
            cart = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
            cart.click()

            # Ждем перехода на страницу корзины
            WebDriverWait(driver, 10).until(EC.url_contains("cart"))

        # 4. Оформление заказа
        with allure.step("4. Оформление заказа"):
            # Ожидаем и кликаем кнопку Checkout
            checkout = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "checkout")))
            checkout.click()

            # Заполняем форму данными
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Иван")
            driver.find_element(By.ID, "last-name").send_keys("Петров")
            driver.find_element(By.ID, "postal-code").send_keys("123456")

            # Продолжаем оформление
            driver.find_element(By.ID, "continue").click()

        # 5. Проверка итоговой стоимости
        with allure.step("5. Проверка итоговой стоимости"):
            # Ожидаем появление элемента с итоговой стоимостью
            total = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))

            # Проверяем что стоимость равна ожидаемой
            assert total.text == "Total: $58.29", f"Ожидалась сумма $58.29, но получили {total.text}"

    except Exception as e:
        # В случае ошибки делаем скриншот
        driver.save_screenshot("error.png")
        raise e
    finally:
        # Закрываем браузер в любом случае
        driver.quit()

