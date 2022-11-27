import pytest
from ui.paths import paths
from selenium.webdriver.support import expected_conditions as EC
from ui.components.header import HeaderComponent
from ui.locators import locators
from ui.base_case.base_case import BaseCase
from _pytest.fixtures import FixtureRequest
import time


class TestHeader(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = HeaderComponent(driver, url_config)

    def test_go_to_mainpage(self):
        self.page.open_path(paths.TACOLAND_DISHES)
        self.page.click(self.page.locators.LOGO_BUTTON)
        assert self.page.is_url(paths.MAIN)

    def test_activate_address(self):
        self.page.click(self.page.locators.ADDRESS_INPUT)
        assert self.page.is_url(paths.SUGGESTS)
        address_elem = self.page.find(self.page.locators.ADDRESS_INPUT)
        assert self.page.is_active(address_elem)
        assert self.page.has_value(address_elem, "")
        assert self.page.is_visible(self.page.locators.SUGGESTS)

    def test_close_address(self):
        self.page.click(self.page.locators.ADDRESS_INPUT)
        assert self.page.is_url(paths.SUGGESTS)
        assert self.page.is_active(self.page.find(self.page.locators.ADDRESS_INPUT))

        suggests_elems = self.page.find_all_elems(self.page.locators.SUGGESTS)
        self.page.click_elem_after(suggests_elems[-1],1)

        assert self.page.is_url(self.page.PATH)
        assert not self.page.is_active(self.page.find(self.page.locators.ADDRESS_INPUT))
        assert self.page.is_invisible(self.page.locators.SUGGESTS)

    def test_open_search(self):
        self.page.click(self.page.locators.SEARCH_BUTTON)
        search_input_elem = self.page.find(self.page.locators.SEARCH_INPUT)
        assert self.page.is_active(search_input_elem)
        assert self.page.has_value(search_input_elem, "")

    def test_close_search(self):
        self.page.click(self.page.locators.SEARCH_BUTTON)
        assert self.page.is_visible(self.page.locators.SEARCH_AREA)

        self.page.click(self.page.locators.SEARCH_CLOSE_BUTTON)
        assert self.page.is_invisible(self.page.locators.SEARCH_AREA)

    def test_go_to_login(self):
        self.page.click(self.page.locators.LOGIN_BUTTON)
        assert self.page.is_url(paths.LOGIN)
        assert self.page.is_visible(self.page.locators.LOGIN_MODAL)

    def test_go_to_profile_menu(self, authorize):
        self.page.click(self.page.locators.PROFILE_BUTTON)
        assert self.page.is_url(paths.PROFILE_MENU)
        assert self.page.is_visible(self.page.locators.PROFILE_MENU)

    def test_close_profile_menu(self, authorize):
        self.page.click(self.page.locators.PROFILE_BUTTON)
        assert self.page.is_url(paths.PROFILE_MENU)
        assert self.page.is_visible(self.page.locators.PROFILE_MENU)

        self.page.click(self.page.locators.PROFILE_BUTTON)
        assert self.page.is_url(self.page.PATH)
        assert self.page.is_invisible(self.page.locators.PROFILE_MENU)

    def test_empty_cart(self, authorize):
        self.page.click(self.page.locators.CART_BUTTON)
        assert self.page.is_url(self.page.PATH)
        assert self.page.is_invisible(self.page.locators.CART)

    def test_open_cart(self,authorize,fill_cart):
        self.page.click(self.page.locators.CART_BUTTON)
        assert self.page.is_url(paths.LOGIN)
        assert self.page.is_visible(self.page.locators.CART)

    def test_close_cart(self,authorize,fill_cart):
        self.page.click(self.page.locators.CART_BUTTON)
        assert self.page.is_url(paths.LOGIN)
        assert self.page.is_visible(self.page.locators.CART)

        self.page.click(self.page.locators.CART_BUTTON)
        assert self.page.is_url(self.page.PATH)
        assert self.page.is_invisible(self.page.locators.CART)
