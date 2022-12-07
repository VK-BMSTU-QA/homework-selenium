import time
from ui.locators import basic_locators

from ui.pages.base_page import BasePage


class FavoritesPage(BasePage):
    locators = basic_locators.FavoritesPageLocators()

    def open(self):
        self.click(BasePage.locators.BUTTON_FAVORITES, 10)
        self.wait_visability_of_elem(
            self.locators.FAVORITES_TEXT, 10
        )

