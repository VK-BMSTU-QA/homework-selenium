import pytest
from ui.paths import paths
from ui.components.cart_page import CartPage
from ui.base_case.base_case import BaseCase


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = CartPage(driver, url_config)

    FIRST_DISH_NUM = 1
    SECOND_DISH_NUM = 2

    def test_decrement_single_dish(self, authorize, set_address):
        self.page.add_to_cart()
        assert self.page.is_url_matches(paths.CART)
        assert self.page.is_visible(self.page.locators.CART)
        assert self.page.is_dish_visible()

        self.page.decrement_dish_in_cart()

        assert self.page.is_invisible(self.page.locators.CART)

    def test_decrement_dish(self, authorize, set_address):
        self.page.add_to_cart()
        self.page.add_to_cart()

        EXPECTED_DISH_COUNT = 2
        assert self.page.get_count_of_dish() == EXPECTED_DISH_COUNT
        assert self.page.get_price_of_dish_in_cart() == self.page.get_price_of_dish_in_menu()

        self.page.decrement_dish_in_cart()

        EXPECTED_DISH_COUNT = 1
        assert self.page.get_count_of_dish() == EXPECTED_DISH_COUNT
        assert self.page.get_price_of_dish_in_cart() == self.page.get_price_of_dish_in_menu()

    def test_increment_dish(self, authorize, set_address):
        self.page.add_to_cart()
        EXPECTED_DISH_COUNT = 1
        assert self.page.get_count_of_dish() == EXPECTED_DISH_COUNT
        assert self.page.get_price_of_dish_in_cart() == self.page.get_price_of_dish_in_menu()

        self.page.increment_dish_in_cart()

        EXPECTED_DISH_COUNT = 2
        assert self.page.get_count_of_dish() == EXPECTED_DISH_COUNT
        assert self.page.get_price_of_dish_in_cart() == self.page.get_price_of_dish_in_menu()

    def test_add_dish_to_cart(self, authorize, set_address):
        self.page.add_to_cart(self.FIRST_DISH_NUM)
        self.page.add_to_cart(self.SECOND_DISH_NUM)
        assert self.page.is_url_matches(paths.CART)
        assert self.page.is_dish_visible(self.FIRST_DISH_NUM)
        assert self.page.is_dish_visible(self.SECOND_DISH_NUM)

    def test_add_dish_to_cart_twice(self, authorize, set_address):
        self.page.add_to_cart()
        self.page.add_to_cart()
        EXPECTED_DISH_COUNT = 2
        assert self.page.get_count_of_dish() == EXPECTED_DISH_COUNT
        assert self.page.get_price_of_dish_in_cart() == self.page.get_price_of_dish_in_menu()

    def test_cart_order(self, authorize, set_address):
        self.page.add_to_cart()
        self.page.click(self.page.locators.ORDER_BUTTON)
        assert self.page.is_url_matches(paths.ORDER)
