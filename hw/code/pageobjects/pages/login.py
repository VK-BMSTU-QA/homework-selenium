from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class LoginPage(Page):

    @property
    def btn_enter(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__block_button")

    @property
    def input_password(self):
        return self.driver.find_element(by=By.ID, value="input_pass")

    @property
    def input_login(self):
        return self.driver.find_element(by=By.ID, value="input_login")
    
    def get_error(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__block_error_text").text

    def open(self, *args, **kwargs):
        super().open("login")

    def fill_login(self, login):
        self.input_login.send_keys(login)

    def fill_password(self, password):
        self.input_password.send_keys(password)

    def login(self, login, password):
        self.fill_login(login)
        self.fill_password(password)
        self.btn_enter.click()
