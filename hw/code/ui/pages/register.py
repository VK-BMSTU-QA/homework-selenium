import time
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class RegPage(BasePage):

    locators = basic_locators.RegisterPageLocators()
    login_url = "https://movie-space.ru/login;"
    url = "https://movie-space.ru/reg"

    def open(self):
        self.click(basic_locators.LoginPageLocators.REGISTER_BUTTON, 10)
        self.wait_visability_of_elem(
            basic_locators.RegisterPageLocators.PASSWORD_COPY_INPUT, 10
        )
