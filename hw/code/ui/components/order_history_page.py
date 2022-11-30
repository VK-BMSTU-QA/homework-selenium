from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class OrderHistoryPage(BaseComponent):
    locators = locators.OrderHistoryLocators()
    PATH = paths.ORDER_HISTORY

    def get_order_details(self):
        self.click(self.locators.DETAILS_BUTTON)
        self.wait_visability_of_elem(self.locators.ORDER_DETAILS)

    def hide_order_details(self):
        self.click(self.locators.DETAILS_BUTTON)
        self.wait_invisability_of_elem(self.locators.ORDER_DETAILS)
