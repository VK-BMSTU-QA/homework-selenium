from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class OrderingPage(BaseComponent):
    locators = locators.OrderingLocators()
    PATH = paths.ORDERING
