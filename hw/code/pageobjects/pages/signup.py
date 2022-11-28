from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class SignUpPage(Page):

    @property
    def btn_enter(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__btn__input")

    @property
    def input_username(self):
        return self.driver.find_element(by=By.ID, value="username")

    @property
    def input_email(self):
        return self.driver.find_element(by=By.ID, value="email")

    @property
    def input_password(self):
        return self.driver.find_element(by=By.ID, value="password")

    @property
    def input_password_repeat(self):
        return self.driver.find_element(by=By.ID, value="repeatpassword")
    
    def get_error_username(self):
        input =  self.driver.find_element(by=By.ID, value="username")
        td_p_input = input.find_element_by_xpath('..')
        return td_p_input.find_element(by=By.CLASS_NAME, value="username").text

    def get_error_email(self):
        input =  self.driver.find_element(by=By.ID, value="email")
        td_p_input = input.find_element_by_xpath('..')
        return td_p_input.find_element(by=By.CLASS_NAME, value="email").text

    def get_error_password(self):
        input =  self.driver.find_element(by=By.ID, value="password")
        td_p_input = input.find_element_by_xpath('..')
        return td_p_input.find_element(by=By.CLASS_NAME, value="password").text
        
    def get_error_password_repeate(self):
        input =  self.driver.find_element(by=By.ID, value="repeatpassword")
        td_p_input = input.find_element_by_xpath('..')
        return td_p_input.find_element(by=By.CLASS_NAME, value="repeatpassword").text
    
    def open(self, *args, **kwargs):
        super().open("register")

    def fill_username(self, username):
        self.input_username.clear()
        self.input_username.send_keys(username)
        self.btn_enter.click()

    def fill_email(self, email):
        self.input_email.clear()
        self.input_email.send_keys(email)
        self.btn_enter.click()

    def fill_password(self, password):
        self.input_password.clear()
        self.input_password.send_keys(password)
        self.btn_enter.click()
    
    def fill_password_repeat(self, password_repeat):
        self.input_password_repeat.clear()
        self.input_password_repeat.send_keys(password_repeat)
        self.btn_enter.click()

    def signup(self, username, email, password1, password2):
        self.fill_username(username)
        self.fill_email(email)
        self.fill_password(password1)
        self.fill_password_repeat(password2)
        self.btn_enter.click()
