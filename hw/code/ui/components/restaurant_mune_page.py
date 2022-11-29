from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class RestaurantMenuPage(BaseComponent):
    locators = locators.RestaurantMenuLocators()
    PATH = paths.GUAVA_DISHES
