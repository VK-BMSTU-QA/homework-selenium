from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class CartPage(BaseComponent):
    locators = locators.CartLocators()
    PATH = paths.GUAVA_DISHES

    def add_to_cart(self, number=1):
        self.click_number(self.locators.ADD_TO_CART_BUTTON, number)

    def is_count_of_dish(self, count, number=1):
        return self.find_all_elems(self.locators.COUNT_OF_DISHES)[number - 1].text == count
