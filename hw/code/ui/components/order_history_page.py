from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class OrderHistoryPage(BaseComponent):
    locators = locators.OrderHistoryLocators()
    PATH = paths.ORDER_HISTORY
