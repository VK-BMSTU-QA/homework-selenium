import pytest
from ui.paths import paths
from ui.components.cart_page import CartPage
from ui.base_case.base_case import BaseCase


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = CartPage(driver, url_config)

    def test_button_minus(self, authorize, set_address):
        self.page.add_to_cart()
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.CART)
        self.page.click(self.page.locators.DECREMENT_DISH_COUNT)
        assert self.page.is_invisible(self.page.locators.CART)

    def test_button_minus_for_some_dishes(self, authorize, set_address):
        self.page.add_to_cart()
        self.page.add_to_cart()
        self.page.click(self.page.locators.DECREMENT_DISH_COUNT)
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.CART)
        assert self.page.is_count_of_dish("1")
        element_price = self.page.find(self.page.locators.PRICE)
        assert self.page.has_text(element_price, "600 ₽")

    def test_button_plus(self, authorize, set_address):
        self.page.add_to_cart()
        self.page.click(self.page.locators.INCREMENT_DISH_COUNT)
        assert self.page.is_count_of_dish("2")
        element_price = self.page.find(self.page.locators.PRICE)
        assert self.page.has_text(element_price, "1200 ₽")

    def test_added_dish_in_cart_for_page_restaurants(self, authorize, set_address):
        self.page.add_to_cart(1)
        self.page.add_to_cart(2)
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.SECOND_DISH_IN_CART)

    def test_added_dish_in_cart_for_page_restaurants(self, authorize, set_address):
        self.page.add_to_cart(1)
        self.page.add_to_cart(2)
        self.page.add_to_cart(2)
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.SECOND_DISH_IN_CART)

        assert self.page.is_count_of_dish("2", 2)

        element_price = self.page.find(self.page.locators.PRICE)
        assert self.page.has_text(element_price, "1760 ₽")

    def test_cart_order(self, authorize, set_address):
        self.page.add_to_cart(1)
        self.page.click(self.page.locators.ORDER_BUTTON)
        assert self.page.is_url(paths.ORDER)
