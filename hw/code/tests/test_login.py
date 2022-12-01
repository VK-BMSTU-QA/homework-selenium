import pytest

from ui.paths import paths
from ui.components.login_page import LoginPage
from ui.base_case.base_case import BaseCase


class TestLogin(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = LoginPage(driver, url_config)

    REGISTERED_PHONE = "+7(901)502-04-56"
    UNREGISTERED_PHONE = "+7(495)000-11-22"
    TOO_SHORT_PHONE = "+7(495)0"

    def test_input_empty_phone(self):
        self.page.click(self.page.locators.LOGIN_BUTTON)
        assert self.page.is_visible(self.page.locators.EMPTY_PHONE_ERROR)

    def test_input_phone_with_small_length(self):
        self.page.input_phone(self.TOO_SHORT_PHONE)
        assert self.page.is_visible(self.page.locators.PHONE_LENGTH_ERROR)

    def test_input_unregistered_phone(self):
        self.page.send_phone(self.UNREGISTERED_PHONE)
        assert self.page.is_visible(self.page.locators.NOT_REGISTERED_PHONE_ERROR)

    def test_input_registered_phone(self):
        self.page.send_phone(self.REGISTERED_PHONE)
        assert self.page.is_visible(self.page.locators.CONFIRM_CODE_HEADER)
        assert self.page.is_url_matches(paths.CONFIRM_CODE)

    def test_register_button_click(self):
        self.page.click(self.page.locators.REGISTER_BUTTON)
        assert self.page.is_url_matches(paths.REGISTER)

    def test_close_modal_window(self):
        self.page.click(self.page.locators.CLOSE_BUTTON)
        assert self.page.is_invisible(self.page.locators.LOGIN_MODAL)
        assert self.page.is_url_matches(paths.MAIN)
