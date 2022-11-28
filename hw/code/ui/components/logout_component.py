from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class LogoutComponent(BaseComponent):
    locators = locators.LogoutLocators()
    PATH = paths.MAIN
