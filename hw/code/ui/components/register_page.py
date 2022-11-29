from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class RegisterPage(BaseComponent):
    locators = locators.RegisterLocators()
    PATH = paths.REGISTER
