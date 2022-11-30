import pytest

from ui.paths import paths
from ui.components.ordering_page import OrderingPage
from ui.base_case.base_case import BaseCase


class TestOrdering(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = OrderingPage(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, set_page):
        self.page.open_path(paths.MAIN)

    def test_back_button_click(self, authorize, fill_cart, open):
        self.page.click(self.page.locators.BACK_BUTTON)
        assert self.page.is_url(paths.GUAVA_DISHES)

    def test_pay_button_click(self, authorize, fill_cart, open):
        self.page.click(self.page.locators.PAY_BUTTON)
        assert self.page.is_visible(self.page.locators.SAVE_SUCCESS)
        assert self.page.is_url(paths.ORDER_HISTORY)
