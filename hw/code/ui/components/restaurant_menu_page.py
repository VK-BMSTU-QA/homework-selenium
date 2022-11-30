from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class RestaurantMenuPage(BaseComponent):
    locators = locators.RestaurantMenuLocators()
    PATH = paths.GUAVA_DISHES

    def add_first_item_to_cart(self):
        self.click(self.locators.ADD_TO_CART_BUTTON)
