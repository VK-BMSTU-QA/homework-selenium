from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class CardPage(BaseComponent):
    locators = locators.CardLocators()
    PATH = paths.GUAVA_DISHES
