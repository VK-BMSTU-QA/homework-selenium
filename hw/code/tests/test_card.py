import pytest
from ui.paths import paths
from selenium.webdriver.support import expected_conditions as EC
from ui.components.card_page import CardPage
from ui.locators import locators
from ui.base_case.base_case import BaseCase
from _pytest.fixtures import FixtureRequest
import time


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = CardPage(driver, url_config)

    def test_button_minus(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.CART)
        self.page.click(self.page.locators.DECREMENT_DISH_COUNT)
        assert not self.page.is_visible(self.page.locators.CART)

    def test_button_minus_for_some_dishes(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.DECREMENT_DISH_COUNT)
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.CART)
        element_count = self.page.find(self.page.locators.COUNT_OF_DISHES)
        assert self.page.has_value_no_input(element_count, "1")
        element_price = self.page.find(self.page.locators.PRICE)
        assert self.page.has_value_no_input(element_price, "600 ₽")

    def test_button_plus(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.INCREMENT_DISH_COUNT)
        element_count = self.page.find(self.page.locators.COUNT_OF_DISHES)
        assert self.page.has_value_no_input(element_count, "2")
        element_price = self.page.find(self.page.locators.PRICE)
        assert self.page.has_value_no_input(element_price, "1200 ₽")

    def test_added_dish_in_card_for_page_restaurants(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.ADD_SECOND_DISH)
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.SECOND_DISH_IN_CARD)

    def test_added_dish_in_card_for_page_restaurants(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.ADD_SECOND_DISH)
        self.page.click(self.page.locators.ADD_SECOND_DISH)
        assert self.page.is_url(paths.CART)
        assert self.page.is_visible(self.page.locators.SECOND_DISH_IN_CARD)

        element_count = self.page.find(self.page.locators.COUNT_SECOND_DISHES)
        assert self.page.has_value_no_input(element_count, "2")

        element_price = self.page.find(self.page.locators.PRICE)
        assert self.page.has_value_no_input(element_price, "1760 ₽")

    def test_card_order(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.ORDER_BUTTON)
        assert self.page.is_url(paths.ORDER)





