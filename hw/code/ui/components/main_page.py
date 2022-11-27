from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class MainPage(BaseComponent):
    locators = locators.MainPageLocators()
    PATH = paths.MAIN
