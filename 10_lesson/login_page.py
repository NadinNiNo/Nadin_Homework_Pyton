from .base_page import BasePage
import allure


class LoginPage(BasePage):
    USERNAME_FIELD = ("id", "user-name")
    PASSWORD_FIELD = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")

    @allure.step("Open login page")
    def open(self) -> None:
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Enter username {username}")
    def enter_username(self, username: str) -> None:
        self.find_element(self.USERNAME_FIELD).send_keys(username)

    @allure.step("Enter password")
    def enter_password(self, password: str) -> None:
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Click login button")
    def click_login(self) -> None:
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Login as {username}")
    def login(self, username: str, password: str) -> None:
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
