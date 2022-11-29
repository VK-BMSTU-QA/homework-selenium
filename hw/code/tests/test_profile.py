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

    def test_input_empty_name(self, authorize):
        self.page.open_path(paths.PROFILE)
        assert self.page.is_url(paths.PROFILE)

        self.page.send_keys_enter(self.page.locators.NAME_INPUT, ' ')
        self.page.click(self.page.locators.SAVE_BUTTON)

        assert self.page.is_visible(self.page.locators.EMPTY_NAME_ERROR)

    def test_input_empty_email(self, authorize):
        self.page.open_path(paths.PROFILE)
        assert self.page.is_url(paths.PROFILE)

        self.page.send_keys_enter(self.page.locators.EMAIL_INPUT, ' ')
        self.page.click(self.page.locators.SAVE_BUTTON)

        assert self.page.is_visible(self.page.locators.EMPTY_EMAIL_ERROR)

    def test_input_valid_name(self, authorize):
        self.page.open_path(paths.PROFILE)
        assert self.page.is_url(paths.PROFILE)

        self.page.send_keys(self.page.locators.NAME_INPUT, 'New name')
        self.page.click(self.page.locators.SAVE_BUTTON)

        assert self.page.is_visible(self.page.locators.SAVE_SUCCESS)

    def test_input_valid_email(self, authorize):
        self.page.open_path(paths.PROFILE)
        assert self.page.is_url(paths.PROFILE)

        self.page.send_keys(self.page.locators.NAME_INPUT, 'new@yandex.ru')
        self.page.click(self.page.locators.SAVE_BUTTON)

        assert self.page.is_visible(self.page.locators.SAVE_SUCCESS)

    def test_upload_valid_avatar(self, authorize):
        self.page.open_path(paths.PROFILE)
        assert self.page.is_url(paths.PROFILE)

        print(os.getcwd() + '/images/avatar.jpeg')

        self.page.click(self.page.locators.AVATAR_BUTTON)
        pyautogui.write(os.getcwd() + '/images/avatar.jpeg')
        pyautogui.press('enter')

        self.page.click(self.page.locators.SAVE_BUTTON)

        assert self.page.is_visible(self.page.locators.SAVE_SUCCESS)

    def test_order_history_button_click(self, authorize):
        self.page.open_path(paths.PROFILE)
        assert self.page.is_url(paths.PROFILE)

        self.page.click(self.page.locators.ORDER_HISTORY_BUTTON)
        assert self.page.is_url(paths.ORDER_HISTORY)

    def test_back_button_click(self, authorize):
        self.page.open_path(paths.PROFILE)
        assert self.page.is_url(paths.PROFILE)

        self.page.click(self.page.locators.BACK_BUTTON)
        assert self.page.is_url(paths.MAIN)
