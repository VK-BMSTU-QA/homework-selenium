from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class HeaderComponent(BaseComponent):
    locators = locators.HeaderLocators()
    PATH = paths.MAIN

    def activate_search_value(self):
        self.click(self.locators.SEARCH_BUTTON)
        return self.get_elem_value(self.locators.SEARCH_INPUT)

    def activate_search(self):
        self.click(self.locators.SEARCH_BUTTON)
        self.wait_visability_of_elem(self.locators.SEARCH_AREA)

    def close_search(self):
        self.click(self.locators.SEARCH_CLOSE_BUTTON)
        self.wait_invisability_of_elem(self.locators.SEARCH_AREA)

    def open_address(self):
        self.click(self.locators.ADDRESS_INPUT)
        self.wait_visability_of_elem(self.locators.SUGGESTS)
        return self.find(self.locators.ADDRESS_INPUT)

    def close_address(self):
        self.click_after(self.locators.LAST_SUGGEST, 1)
        self.wait_invisability_of_elem(self.locators.SUGGESTS)

    def open_cart(self):
        self.click(self.locators.CART_BUTTON)
        self.wait_visability_of_elem(self.locators.CART)

    def try_open_cart(self):
        self.click(self.locators.CART_BUTTON)

    def close_cart(self):
        self.click(self.locators.CART_BUTTON)
        self.wait_invisability_of_elem(self.locators.CART)

    def go_to_login(self):
        self.click(self.locators.LOGIN_BUTTON)
        self.wait_visability_of_elem(self.locators.LOGIN_MODAL)

    def open_profile_menu(self):
        self.click(self.locators.PROFILE_BUTTON)
        self.wait_visability_of_elem(self.locators.PROFILE_MENU)

    def close_profile_menu(self):
        self.click(self.locators.PROFILE_BUTTON)
        self.wait_invisability_of_elem(self.locators.PROFILE_MENU)

    def click_to_logo(self):
        self.click(self.locators.LOGO_BUTTON)
        self.wait_visability_of_elem(self.locators.RESTAURANTS_HEADER)
