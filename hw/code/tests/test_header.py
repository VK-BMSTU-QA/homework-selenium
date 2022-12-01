import pytest
from ui.paths import paths
from ui.components.header import HeaderComponent
from ui.base_case.base_case import BaseCase


class TestHeader(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = HeaderComponent(driver, url_config)

    def test_go_to_mainpage(self):
        self.page.open_path(paths.TACOLAND_DISHES)
        self.page.click_to_logo()
        assert self.page.is_visible(self.page.locators.RESTAURANTS_HEADER)
        assert self.page.is_url_matches(paths.MAIN)

    def test_activate_address(self):
        address_elem = self.page.open_address()
        assert self.page.is_url_matches(paths.SUGGESTS)
        assert self.page.is_active(address_elem)
        assert self.page.has_value(address_elem, "")
        assert self.page.is_visible(self.page.locators.SUGGESTS)

    def test_close_address(self):
        address_elem = self.page.open_address()
        assert self.page.is_url_matches(paths.SUGGESTS)
        assert self.page.is_active(address_elem)

        self.page.close_address()
        assert self.page.is_invisible(self.page.locators.SUGGESTS)
        assert self.page.is_url_matches(self.page.PATH)
        assert self.page.is_not_active(self.page.find(self.page.locators.ADDRESS_INPUT))

    def test_open_search(self):
        search_input_elem, search_input_value = self.page.activate_search_value()
        assert self.page.is_active(search_input_elem)
        assert search_input_value == ""

    def test_close_search(self):
        self.page.activate_search()
        assert self.page.is_visible(self.page.locators.SEARCH_AREA)

        self.page.close_search()
        assert self.page.is_invisible(self.page.locators.SEARCH_AREA)

    def test_go_to_login(self):
        self.page.go_to_login()
        assert self.page.is_visible(self.page.locators.LOGIN_MODAL)
        assert self.page.is_url_matches(paths.LOGIN)

    def test_go_to_profile_menu(self, authorize):
        self.page.open_profile_menu()
        assert self.page.is_visible(self.page.locators.PROFILE_MENU)
        assert self.page.is_url_matches(paths.PROFILE_MENU)

    def test_close_profile_menu(self, authorize):
        self.page.open_profile_menu()
        assert self.page.is_url_matches(paths.PROFILE_MENU)
        assert self.page.is_visible(self.page.locators.PROFILE_MENU)

        self.page.close_profile_menu()
        assert self.page.is_url_matches(self.page.PATH)
        assert self.page.is_invisible(self.page.locators.PROFILE_MENU)

    def test_empty_cart(self, authorize):
        self.page.try_open_cart()
        assert self.page.is_invisible(self.page.locators.CART)
        assert self.page.is_url_matches(self.page.PATH)

    def test_open_cart(self, authorize, fill_cart):
        self.page.open_cart()
        assert self.page.is_visible(self.page.locators.CART)
        assert self.page.is_url_matches(paths.LOGIN)

    def test_close_cart(self, authorize, fill_cart):
        self.page.open_cart()
        assert self.page.is_visible(self.page.locators.CART)
        assert self.page.is_url_matches(paths.LOGIN)

        self.page.close_cart()
        assert self.page.is_invisible(self.page.locators.CART)
        assert self.page.is_url_matches(self.page.PATH)
