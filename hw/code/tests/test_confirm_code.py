import pytest

from ui.paths import paths
from ui.components.login_page import LoginPage
from ui.base_case.base_case import BaseCase


class TestConfirmCode(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = LoginPage(driver, url_config)

    @pytest.fixture(scope="function")
    def send_default_phone(self):
        self.page.send_phone()

    invalid_code = "0000"
    valid_code = "1111"

    def test_input_empty_code(self, send_default_phone):
        self.page.click(self.page.locators.CONFIRM_CODE_BUTTON)

        assert self.page.is_visible(self.page.locators.INVALID_CODE_ERROR)

    def test_input_invalid_code(self, send_default_phone):
        self.page.send_code_to_confirm(self.invalid_code)
        assert self.page.is_visible(self.page.locators.INVALID_CODE_ERROR)

    def test_input_valid_code(self, send_default_phone):
        self.page.send_code_to_confirm(self.valid_code)
        assert self.page.is_visible(self.page.locators.PROFILE_BUTTON)

    def test_retry_button_click(self, send_default_phone):
        self.page.click(self.page.locators.RETRY_BUTTON)
        assert self.page.is_visible(self.page.locators.RETRY_SUCCESS)

    def test_close_modal_window(self, send_default_phone):
        self.page.click(self.page.locators.CLOSE_BUTTON)
        assert self.page.is_url_matches(paths.MAIN)
