import os

import pytest
import pyautogui

from ui.paths import paths
from ui.components.profile_page import ProfilePage
from ui.base_case.base_case import BaseCase


class TestProfile(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = ProfilePage(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, set_page):
        self.page.open_path(paths.MAIN)

    def test_input_empty_name(self, authorize,open):
        self.page.send_new_name(' ')
        assert self.page.is_visible(self.page.locators.EMPTY_NAME_ERROR)

    def test_input_empty_email(self, authorize,open):
        self.page.send_new_email(' ')

        assert self.page.is_visible(self.page.locators.EMPTY_EMAIL_ERROR)

    def test_input_valid_name(self, authorize,open):
        self.page.send_new_name('New name')
        assert self.page.is_visible(self.page.locators.SAVE_SUCCESS)

    def test_input_valid_email(self, authorize,open):
        self.page.send_new_email('new@yandex.ru')
        assert self.page.is_visible(self.page.locators.SAVE_SUCCESS)

    def test_upload_valid_avatar(self, authorize,open):
        print(os.getcwd() + '/images/avatar.jpeg')

        self.page.click(self.page.locators.AVATAR_BUTTON)
        pyautogui.write(os.getcwd() + '/images/avatar.jpeg')
        pyautogui.press('enter')

        self.page.click(self.page.locators.SAVE_BUTTON)

        assert self.page.is_visible(self.page.locators.SAVE_SUCCESS)

    def test_order_history_button_click(self, authorize,open):
        self.page.click(self.page.locators.ORDER_HISTORY_BUTTON)
        assert self.page.is_url(paths.ORDER_HISTORY)

    def test_back_button_click(self, authorize,open):
        self.page.click(self.page.locators.BACK_BUTTON)
        assert self.page.is_url(paths.MAIN)
