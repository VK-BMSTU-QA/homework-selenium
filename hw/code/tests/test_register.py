import pytest

from ui.paths import paths
from ui.components.register_page import RegisterPage
from ui.base_case.base_case import BaseCase
from ui.locators import locators


class TestRegister(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = RegisterPage(driver, url_config)
        self

    VALID_EMAIL = "user@yandex.ru"
    REGISTERED_PHONE = "+7(901)502-04-56"
    UNREGISTERED_PHONE = "+7(495)000-11-22"
    EMPY = ""
    USERNAME = "user"
    INVALID_EMAIL = "user"
    TOO_SHORT_PHONE = "+7(495)0"

    @pytest.mark.parametrize(
        "phone,username,email,expected_error_locator",
        [
            (EMPY, USERNAME, VALID_EMAIL, locators.RegisterLocators.EMPTY_PHONE_ERROR),
            (UNREGISTERED_PHONE, EMPY, VALID_EMAIL, locators.RegisterLocators.EMPTY_NAME_ERROR),
            (UNREGISTERED_PHONE, USERNAME, EMPY, locators.RegisterLocators.EMPTY_EMAIL_ERROR),
        ],
    )
    def test_empty_field_in_register_data(self, phone, username, email, expected_error_locator):
        self.page.send_register_data(phone, username, email)
        assert self.page.is_visible(expected_error_locator)

    def test_input_phone_with_small_length(self):
        self.page.send_phone(self.TOO_SHORT_PHONE)
        assert self.page.is_visible(self.page.locators.PHONE_LENGTH_ERROR)

    def test_input_invalid_email(self):
        self.page.send_email(self.INVALID_EMAIL)
        assert self.page.is_visible(self.page.locators.INVALID_EMAIL_ERROR)

    def test_input_registered_phone(self):
        self.page.send_register_data(self.REGISTERED_PHONE, self.USERNAME, self.VALID_EMAIL)
        assert self.page.is_visible(self.page.locators.REGISTERED_PHONE_ERROR)

    def test_input_not_registered_phone(self):
        self.page.send_register_data(self.UNREGISTERED_PHONE, self.USERNAME, self.VALID_EMAIL)
        assert self.page.is_visible(self.page.locators.CONFIRM_CODE_HEADER)
        assert self.page.is_url_matches(paths.CONFIRM_CODE)

    def test_login_button_click(self):
        self.page.click(self.page.locators.LOGIN_BUTTON)
        assert self.page.is_url_matches(paths.LOGIN)

    def test_close_modal_window(self):
        self.page.click(self.page.locators.CLOSE_BUTTON)
        assert self.page.is_url_matches(paths.MAIN)
