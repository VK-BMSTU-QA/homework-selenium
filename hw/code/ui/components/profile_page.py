from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class ProfilePage(BaseComponent):
    locators = locators.ProfileLocators()
    PATH = paths.MAIN
