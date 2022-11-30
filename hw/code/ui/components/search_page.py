from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class SearchPage(BaseComponent):
    locators = locators.SearchPageLocators()
    PATH = paths.SEARCH

    def search_with_result(self, query):
        self.click(self.locators.SEARCH_BUTTON)
        self.wait_visability_of_elem(self.locators.SEARCH_AREA)
        with self.wait_for_reload_elem(self.locators.RESTAURANT_CART):
            self.send_keys_enter(self.locators.SEARCH_INPUT, query)

    def search_wrong(self, query):
        self.click(self.locators.SEARCH_BUTTON)
        self.wait_visability_of_elem(self.locators.SEARCH_AREA)
        self.send_keys_enter(self.locators.SEARCH_INPUT, query)
        self.wait_visability_of_elem(self.locators.UI_NOTIFICATION)

    def is_first_result(self, restaurant):
        return self.find(self.locators.RESTAURANT_CART_NAME).text.lower() == restaurant.lower()

    def has_results(self):
        return self.is_visible(self.locators.RESTAURANT_CART_NAME)

    def have_nothing_found(self):
        return self.is_visible(self.locators.NOTHING_FOUND_MESSAGE)

    def is_query_too_long(self):
        return self.is_visible(self.locators.TOO_LONG_UI_NOTIFICATION)
