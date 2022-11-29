from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class CommentsElement(BaseComponent):
    locators = locators.CommentsLocators()
    PATH = paths.MAIN
