import pytest

from ui.paths import paths
from ui.components.login_page import LoginPage
from ui.base_case.base_case import BaseCase


class TestLogin(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = LoginPage(driver, url_config)

    def test_input_empty_phone(self):
        self.page.click(self.page.locators.LOGIN_BUTTON)

        assert self.page.is_visible(self.page.locators.EMPTY_PHONE_ERROR)

    def test_input_phone_with_small_length(self):
        self.page.send_keys(self.page.locators.PHONE_INPUT, '+7(495')

        assert self.page.is_visible(self.page.locators.PHONE_LENGTH_ERROR)

    def test_input_not_registered_phone(self):
        self.page.send_keys(self.page.locators.PHONE_INPUT, '+7(495)000-11-22')
        self.page.click(self.page.locators.LOGIN_BUTTON)

        assert self.page.is_visible(self.page.locators.NOT_REGISTERED_PHONE_ERROR)

    def test_input_registered_phone(self):
        self.page.send_keys(self.page.locators.PHONE_INPUT, '+7(901)502-04-56')
        self.page.click(self.page.locators.LOGIN_BUTTON)

        assert self.page.is_url(paths.CONFIRM_CODE)

    def test_register_button_click(self):
        self.page.click(self.page.locators.REGISTER_BUTTON)

        assert self.page.is_url(paths.REGISTER)

    def test_close_modal_window(self):
        self.page.click(self.page.locators.CLOSE_BUTTON)

        assert self.page.is_url(paths.MAIN)
