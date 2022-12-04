from hw.code.ui.locators import basic_locators
from hw.code.ui.pages.base_page import BasePage


class LoginPage(BasePage):

    locators = basic_locators.LoginPageLocators()
    url = 'https://movie-space.ru/login;'

    def login(self, login, password):
        login_input = self.find(self.locators.LOGIN_INPUT, 10)
        self.send_keys(login_input,login)
        password_input = self.find(self.locators.PASSWORD_INPUT, 10)
        self.send_keys(password_input, password)
        self.click((self.locators.PASS_LOGIN_CREDS_BUTTON), 10)
