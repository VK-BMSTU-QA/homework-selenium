import time
import pytest

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from ui.base_case import BaseCase
from ui.pages.login import LoginPage


class TestLogin:

    def test_login(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)

        credentials = request.getfixturevalue("credentials")
        login_page = LoginPage(driver)
        login_page.login(*credentials)


class TestLoginErrors:
    url = "https://movie-space.ru/login"
    EMPTY_PASS = "empty_pass"
    EMPTY_EMAIL = "empty_email"
    RANDOM_EMAIL = "2356fhnudffjrmcuawerl@gogol.ya"
    RANDOM_PASS = "random_unknown_password_hgyur34rtyrfq34134fjiu"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)

        self.login_input = self.login_page.find(
            self.login_page.locators.LOGIN_INPUT, 10
        )
        self.password_input = self.login_page.find(
            self.login_page.locators.PASSWORD_INPUT, 10
        )

    def test_wrong_input_notifications(self):
        self.login_page.send_keys(self.login_input, self.EMPTY_EMAIL)
        self.login_page.send_keys(self.password_input, self.EMPTY_PASS)

        notification = self.login_page.wait_visability_of_elem(
            self.login_page.locators.LOGIN_NOTIFICATION
        )

        assert str(notification.text) == "Введите действительный email"

        self.login_page.send_keys(self.login_input, self.EMPTY_EMAIL)
        self.login_page.send_keys(self.login_input, "")
        self.login_page.send_keys(self.password_input, "")

        notification = self.login_page.wait_visability_of_elem(
            self.login_page.locators.LOGIN_NOTIFICATION
        )

        assert str(notification.text) == "Заполните поле"

        self.login_page.send_keys(self.password_input, self.EMPTY_PASS)
        self.login_page.send_keys(self.password_input, "")
        self.login_page.send_keys(self.login_input, "")

        notification = self.login_page.wait_visability_of_elem(
            self.login_page.locators.PASSWORD_NOTIFICATION
        )

        assert str(notification.text) == "Заполните поле"

    def test_user_unexist(self):
        self.login_page.send_keys(self.login_input, self.RANDOM_EMAIL)
        self.login_page.send_keys(self.password_input, self.RANDOM_PASS)

        self.login_page.click(
            self.login_page.locators.PASS_LOGIN_CREDS_BUTTON, 10
        )

        notification = self.login_page.wait_visability_of_elem(
            self.login_page.locators.USER_DOES_NOT_EXISTS_NOTIFICATION
        )

        assert str(notification.text) == "Неверный логин или пароль"
