import pytest

from ui.paths import paths
from ui.components.login_page import LoginPage
from ui.base_case.base_case import BaseCase


class TestConfirmCode(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = LoginPage(driver, url_config)

    def test_input_empty_code(self):
        self.page.send_keys(self.page.locators.PHONE_INPUT, '+7(901)502-04-56')
        self.page.click(self.page.locators.LOGIN_BUTTON)

        assert self.page.is_url(paths.CONFIRM_CODE)

        self.page.click(self.page.locators.CONFIRM_CODE_BUTTON)

        assert self.page.is_visible(self.page.locators.INVALID_CODE_ERROR)

    def test_input_invalid_code(self):
        self.page.send_keys(self.page.locators.PHONE_INPUT, '+7(901)502-04-56')
        self.page.click(self.page.locators.LOGIN_BUTTON)

        assert self.page.is_url(paths.CONFIRM_CODE)

        self.page.send_keys(self.page.locators.CODE_INPUT, '0000')
        self.page.click(self.page.locators.CONFIRM_CODE_BUTTON)

        assert self.page.is_visible(self.page.locators.INVALID_CODE_ERROR)

    def test_input_valid_code(self):
        self.page.send_keys(self.page.locators.PHONE_INPUT, '+7(901)502-04-56')
        self.page.click(self.page.locators.LOGIN_BUTTON)

        assert self.page.is_url(paths.CONFIRM_CODE)

        self.page.send_keys(self.page.locators.CODE_INPUT, '1111')
        self.page.click(self.page.locators.CONFIRM_CODE_BUTTON)

        assert self.page.is_visible(self.page.locators.PROFILE_BUTTON)

    def test_retry_button_click(self):
        self.page.send_keys(self.page.locators.PHONE_INPUT, '+7(901)502-04-56')
        self.page.click(self.page.locators.LOGIN_BUTTON)

        assert self.page.is_url(paths.CONFIRM_CODE)

        self.page.click(self.page.locators.RETRY_BUTTON)

        assert self.page.is_visible(self.page.locators.RETRY_SUCCESS)

    def test_close_modal_window(self):
        self.page.send_keys(self.page.locators.PHONE_INPUT, '+7(901)502-04-56')
        self.page.click(self.page.locators.LOGIN_BUTTON)

        assert self.page.is_url(paths.MAIN)
