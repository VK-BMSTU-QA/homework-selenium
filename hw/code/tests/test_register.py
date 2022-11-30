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

    @pytest.mark.parametrize(
        "phone,username,email,expected_error_locator",
        [
            ("", "user", "user@yandex.ru", locators.RegisterLocators.EMPTY_PHONE_ERROR),
            ("+7(901)502-04-56", "", "user@yandex.ru", locators.RegisterLocators.EMPTY_NAME_ERROR),
            ("+7(901)502-04-56", "user", "", locators.RegisterLocators.EMPTY_EMAIL_ERROR),
        ],
    )
    def test_empty_field_in_register_data(self, phone, username, email, expected_error_locator):
        self.page.send_register_data(phone, username, email)
        assert self.page.is_visible(expected_error_locator)

    def test_input_phone_with_small_length(self):
        self.page.send_phone("+7(901)")
        assert self.page.is_visible(self.page.locators.PHONE_LENGTH_ERROR)

    def test_input_invalid_email(self):
        self.page.send_email("test")
        assert self.page.is_visible(self.page.locators.INVALID_EMAIL_ERROR)

    def test_input_registered_phone(self):
        self.page.send_register_data("+7(901)502-04-56", "user", "user@yandex.ru")
        assert self.page.is_visible(self.page.locators.REGISTERED_PHONE_ERROR)

    def test_input_not_registered_phone(self):
        self.page.send_register_data("+7(495)000-11-22", "user", "user@yandex.ru")
        assert self.page.is_visible(self.page.locators.CONFIRM_CODE_HEADER)
        assert self.page.is_url(paths.CONFIRM_CODE)

    def test_login_button_click(self):
        self.page.click(self.page.locators.LOGIN_BUTTON)
        assert self.page.is_url(paths.LOGIN)

    def test_close_modal_window(self):
        self.page.click(self.page.locators.CLOSE_BUTTON)
        assert self.page.is_url(paths.MAIN)
