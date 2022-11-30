import pytest
from ui.paths import paths
from ui.components.main_page import MainPage
from ui.base_case.base_case import BaseCase


class TestMainPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = MainPage(driver, url_config)

    def test_go_to_restaurant_menu(self):
        self.page.click(self.page.locators.GUAVA_RESTAURANT_IMG)
        assert self.page.is_visible(self.page.locators.MENU_HEADER)
        assert self.page.is_url(paths.GUAVA_DISHES)

    def test_choose_category(self):
        self.page.choose_sushi_category()
        assert self.page.is_visible(self.page.locators.SUSHI_CATEGORY_SELECTED_BUTTON)
        assert self.page.is_url(paths.SUSHI_CATEGORY)

    def test_unchoose_category(self):
        self.page.choose_sushi_category()
        assert self.page.is_visible(self.page.locators.SUSHI_CATEGORY_SELECTED_BUTTON)
        assert self.page.is_url(paths.SUSHI_CATEGORY)

        self.page.unchoose_sushi_category()
        assert self.page.is_invisible(self.page.locators.SUSHI_CATEGORY_SELECTED_BUTTON)
        assert self.page.is_url(paths.MAIN)

    def test_change_category(self):
        self.page.choose_sushi_category()
        assert self.page.is_visible(self.page.locators.SUSHI_CATEGORY_SELECTED_BUTTON)
        assert self.page.is_url(paths.SUSHI_CATEGORY)

        self.page.choose_pizza_category()
        assert self.page.is_url(paths.PIZZA_CATEGORY)
        assert self.page.is_visible(self.page.locators.PIZZA_CATEGORY_SELECTED_BUTTON)
        assert self.page.is_invisible(self.page.locators.SUSHI_CATEGORY_SELECTED_BUTTON)

    def test_apply_promocode(self, authorize, set_address):
        self.page.click(self.page.locators.PROMOCODE_IMG)
        assert self.page.is_visible(self.page.locators.PROMOCODE_UI_NOTIFICATION)
        assert self.page.is_visible(self.page.locators.MENU_HEADER)
        assert self.page.is_url(paths.CART)
