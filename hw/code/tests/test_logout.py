import pytest

from ui.paths import paths
from ui.components.logout_component import LogoutComponent
from ui.base_case.base_case import BaseCase


class TestLogout(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = LogoutComponent(driver, url_config)

    def test_logout_from_profile(self, authorize):
        self.page.open_path(paths.PROFILE)
        assert self.page.is_url(paths.PROFILE)

        self.page.click(self.page.locators.PROFILE_BUTTON)
        assert self.page.is_url(paths.PROFILE_MENU)

        self.page.click(self.page.locators.LOGOUT_BUTTON)
        assert self.page.is_url(paths.MAIN)

    def test_logout_from_restaurant(self, authorize):
        self.page.open_path(paths.GUAVA_DISHES)
        assert self.page.is_url(paths.GUAVA_DISHES)

        self.page.click(self.page.locators.PROFILE_BUTTON)
        assert self.page.is_url(paths.PROFILE_MENU)

        self.page.click(self.page.locators.LOGOUT_BUTTON)
        assert self.page.is_url(paths.GUAVA_DISHES)

    def test_logout_from_order_history(self, authorize, set_address, fill_cart):
        self.page.open_path(paths.ORDERING)
        assert self.page.is_url(paths.ORDERING)

        self.page.click(self.page.locators.PAY_BUTTON)
        assert self.page.is_url(paths.ORDER_HISTORY)

        self.page.click(self.page.locators.PROFILE_BUTTON)
        assert self.page.is_url(paths.PROFILE_MENU)

        self.page.click(self.page.locators.LOGOUT_BUTTON)
        assert self.page.is_url(paths.MAIN)
