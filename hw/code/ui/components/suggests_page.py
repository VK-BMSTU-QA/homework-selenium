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
        PIXEL_OFFSET_AFTER_ADDRESS = 1
        with self.wait_for_reload_elem(self.locators.ADDRESS_INPUT):
            self.click_after(self.locators.LAST_SUGGEST, PIXEL_OFFSET_AFTER_ADDRESS)
        self.wait_invisability_of_elem(self.locators.SUGGESTS)

    def get_address_value(self):
        address_input_elem = self.find(self.locators.ADDRESS_INPUT)
        return address_input_elem, self.get_value(address_input_elem)

    def get_address_input(self):
        return self.find(self.locators.ADDRESS_INPUT)

    def get_suggests(self, query):
        time.sleep(self.DEBOUNCE_TIMEOUT)
        with self.wait_for_reload_elem(self.locators.SUGGESTS):
            self.send_keys_no_clear(self.locators.ADDRESS_INPUT, query)

    def get_text_first_suggest(self, value):
        return self.get_text(self.find(self.locators.SUGGESTS))

    def choose_first_suggest(self):
        with self.wait_for_reload_elems(self.default_timeout, self.locators.SUGGESTS, self.locators.ADDRESS_INPUT):
            self.click(self.locators.SUGGESTS)

    def get_suggests_full_address(self, address):
        self.get_suggests(address[:-1])
        self.get_suggests(address[-1])

    def get_text_first_suggest(self):
        return self.get_text(self.locators.SUGGESTS)
