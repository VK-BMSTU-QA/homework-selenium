from .base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .locators.auth_reg import AuthLocators


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, add_url="login")   
    
    def login(self, login, password):
        login_input = self.find_element(AuthLocators.LOGIN_INPUT)
        login_input.clear()
        login_input.send_keys(login)
        password_input = self.find_element(AuthLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        login_button = self.find_element(AuthLocators.LOGIN_BUTTON)
        login_button.click()

    def get_error_messages(self):
        error_messages = self.find_elements(AuthLocators.ANY_ERROR, soft=True)
        return [message.text for message in error_messages]

    def is_login_error(self) -> bool:
        return self.is_elem(AuthLocators.LOGIN_ERROR, soft=True)

    def is_password_error(self) -> bool:
        return self.is_elem(AuthLocators.PASSWORD_ERROR, soft=True)

    def is_redirected(self) -> bool:
        return self.is_url_endswith('income')

    def go_to_register(self):
        from .register import RegisterPage
        register_button = self.find_element(AuthLocators.REGISTER_BUTTON)
        register_button.click()
        register = RegisterPage(self.driver)
        assert register.is_loaded()
        return register

    def is_loaded(self) -> bool:
        try:
            elem = self.find_element(AuthLocators.LOGIN_BUTTON)
            return elem.is_displayed()
        except TimeoutException:
            return False
