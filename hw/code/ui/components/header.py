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

    def close_search(self):
        self.click(self.locators.SEARCH_CLOSE_BUTTON)

    def open_address(self):
        self.click(self.locators.ADDRESS_INPUT)
        self.wait_visability_of_elem(self.locators.SUGGESTS)
        return self.find(self.locators.ADDRESS_INPUT)

    def close_address(self):
        self.click_after(self.locators.LAST_SUGGEST, 1)
        self.wait_invisability_of_elem(self.locators.SUGGESTS)
