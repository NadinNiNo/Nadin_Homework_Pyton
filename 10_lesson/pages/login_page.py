import allure
from .base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    """Класс для страницы авторизации"""

    USERNAME_FIELD = ("id", "user-name")
    PASSWORD_FIELD = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """Открыть страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести логин {username}")
    def enter_username(self, username: str) -> None:
        """
        Ввести имя пользователя
        :param username: str - имя пользователя
        """
        self.find_element(self.USERNAME_FIELD).send_keys(username)

    @allure.step("Ввести пароль {password}")
    def enter_password(self, password: str) -> None:
        """
        Ввести пароль
        :param password: str - пароль
        """
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> None:
        """Нажать кнопку входа"""
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Авторизоваться как {username}")
    def login(self, username: str, password: str) -> None:
        """
        Полная авторизация
        :param username: str - имя пользователя
        :param password: str - пароль
        """
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
