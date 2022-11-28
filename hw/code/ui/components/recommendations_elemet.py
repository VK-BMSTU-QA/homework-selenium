from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class RecommendationsElement(BaseComponent):
    locators = locators.RecommendationsLocators()
    PATH = paths.MAIN
