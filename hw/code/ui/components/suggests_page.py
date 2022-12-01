from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths
import time


class SuggestPage(BaseComponent):
    locators = locators.SuggestPageLocators()
    PATH = paths.SUGGESTS
    DEBOUNCE_TIMEOUT = 1

    def activate_address_input(self):
        search_input = self.click(self.locators.ADDRESS_INPUT)
        self.wait_visability_of_elem(self.locators.SUGGESTS)
        return search_input

    def close_address_input(self):
        self.click_after(self.locators.LAST_SUGGEST, 1)
        self.wait_invisability_of_elem(self.locators.SUGGESTS)

    def get_address_value(self):
        return self.get_elem_value(self.locators.ADDRESS_INPUT)

    def is_address_value(self, value):
        return self.get_elem_value(self.locators.ADDRESS_INPUT) == value

    def get_address_input(self):
        return self.find(self.locators.ADDRESS_INPUT)

    def get_suggests(self, query):
        with self.wait_for_reload_elem(self.locators.SUGGESTS):
            self.send_keys_no_clear(self.locators.ADDRESS_INPUT, query)

    def is_first_suggest(self, value):
        return self.has_text(self.find(self.locators.SUGGESTS), value)

    def choose_first_suggest(self):
        with self.wait_for_reload_elem(self.locators.SUGGESTS):
            self.click(self.locators.SUGGESTS)

    def get_suggests_full_address(self, address):
        self.get_suggests(address[:-1])
        time.sleep(self.DEBOUNCE_TIMEOUT)
        self.get_suggests(address[-1])

    def get_elem_text_first_suggest(self):
        return self.get_elem_text(self.locators.SUGGESTS)[1]
