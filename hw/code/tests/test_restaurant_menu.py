import pytest
from ui.paths import paths
from ui.components.restaurant_menu_page import RestaurantMenuPage
from ui.base_case.base_case import BaseCase


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = RestaurantMenuPage(driver, url_config)

    def test_add_to_cart(self, authorize, set_address):
        self.page.add_first_item_to_cart()
        assert self.page.is_visible(self.page.locators.CART)
        assert self.page.is_url(paths.CART)

    def test_redirect_button_all_restaurants(self):
        self.page.click(self.page.locators.ALL_RESTAURANTS_BUTTON)
        assert self.page.is_visible(self.page.locators.RESTAURANTS_LIST)
        assert self.page.is_url(paths.MAIN)

    def test_no_auth_add_to_cart_redirect_to_login(self):
        self.page.add_first_item_to_cart()
        assert self.page.is_url(paths.LOGIN)

