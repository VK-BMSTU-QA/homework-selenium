from selenium.webdriver.common.by import By

from pageobjects.base.page import Page
from utils.constants import default_password
from pageobjects.components.header import Header
import time


class SignUpPage(Page):

    @property
    def btn_enter(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__block_button")

    @property
    def input_password1(self):
        return self.driver.find_element(by=By.ID, value="input_pass")

    @property
    def input_password2(self):
        return self.driver.find_element(by=By.ID, value="input_pass_rep")

    @property
    def input_login(self):
        return self.driver.find_element(by=By.ID, value="input_login")
    
    def get_error(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__block_error_text").text

    def open(self, *args, **kwargs):
        super().open("signup")

    def fill_login(self, login):
        self.input_login.send_keys(login)

    def fill_password1(self, password):
        self.input_password1.send_keys(password)
    
    def fill_password2(self, password):
        self.input_password2.send_keys(password)

    def signup(self, login, password1, password2):
        self.fill_login(login)
        self.fill_password1(password1)
        self.fill_password2(password2)
        self.btn_enter.click()

    def signup_new_user(self):
        login = time.time()
        print('current login:', login)
        self.signup(login, default_password, default_password)
        Header.create(self.driver)

