import time
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class ProfilePage(BasePage):

    locators = basic_locators.ProfilePageLocators()
    url = "https://movie-space.ru/profile"

    def open(self):
        self.click(basic_locators.BasePageLocators.BUTTON_PROFILE_1, 10)
        self.wait_visability_of_elem(
            basic_locators.ProfilePageLocators.SAVE_BUTTON, 10
        )
