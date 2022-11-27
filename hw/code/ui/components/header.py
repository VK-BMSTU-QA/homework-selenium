from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class HeaderComponent(BaseComponent):
    locators = locators.HeaderLocators()
    PATH = paths.MAIN
