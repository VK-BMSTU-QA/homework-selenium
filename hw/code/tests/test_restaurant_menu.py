import pytest
from ui.paths import paths
from selenium.webdriver.support import expected_conditions as EC
from ui.components.restaurant_mune_page import RestaurantMenuPage
from ui.locators import locators
from ui.base_case.base_case import BaseCase
from _pytest.fixtures import FixtureRequest
import time


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = RestaurantMenuPage(driver, url_config)

    def test_add_to_cart(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.CART)

    def test_redirect_button_all_restaurants(self):
        self.page.click(self.page.locators.FOBRINGTO_BUTTON)
        assert self.page.is_url(paths.MAIN)
        assert self.page.is_visible(self.page.locators.RESTAURANTS_LIST)

    def test_no_auth_add_to_card_redirect_to_login(self):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        assert self.page.is_url(paths.LOGIN)

