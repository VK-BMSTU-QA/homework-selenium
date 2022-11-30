from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class RecommendationsElement(BaseComponent):
    locators = locators.RecommendationsLocators()
    PATH = paths.GUAVA_DISHES

    def add_to_cart(self):
        self.click(self.locators.ADD_TO_CART_BUTTON)

    def add_recommendation(self):
        self.click(self.locators.ADD_RECOMMENDATIONS)
