from .base import BasePage
from .locators.auth_reg import RegisterLocators
from selenium.common.exceptions import TimeoutException

class RegisterPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, add_url="registration")
        # wait for page to load
        self.find_element(RegisterLocators.REGISTER_BUTTON)
        self.data = {
            'first_name': self.is_first_name_error,
            'last_name': self.is_last_name_error,
            'login': self.is_login_error,
            'password': self.is_password_error,
            'confirm_password': self.is_confirm_password_error,
        }


    def register(self, first_name, last_name, login, password, confirm_password):
        first_name_input = self.find_element(RegisterLocators.FIRSTNAME_INPUT)
        first_name_input.clear()
        first_name_input.send_keys(first_name)
        last_name_input = self.find_element(RegisterLocators.LASTNAME_INPUT)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        login_input = self.find_element(RegisterLocators.LOGIN_INPUT)
        login_input.clear()
        login_input.send_keys(login)
        password_input = self.find_element(RegisterLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        confirm_password_input = self.find_element(RegisterLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.clear()
        confirm_password_input.send_keys(confirm_password)
        register_button = self.find_element(RegisterLocators.REGISTER_BUTTON)
        register_button.click()

    def get_error_messages(self):
        error_messages = self.find_elements(RegisterLocators.ANY_ERROR, soft=True)
        return [message.text for message in error_messages]

    def is_first_name_error(self) -> bool:
        return self.is_elem(RegisterLocators.FIRSTNAME_ERROR, soft=True)

    def is_last_name_error(self) -> bool:
        return self.is_elem(RegisterLocators.LASTNAME_ERROR, soft=True)

    def is_login_error(self) -> bool:
        return self.is_elem(RegisterLocators.LOGIN_ERROR, soft=True)

    def is_password_error(self) -> bool:
        return self.is_elem(RegisterLocators.PASSWORD_ERROR, soft=True)

    def is_confirm_password_error(self) -> bool:
        return self.is_elem(RegisterLocators.CONFIRM_PASSWORD_ERROR, soft=True)

    def is_redirected(self) -> bool:
        return self.is_url_endswith('income')

    def go_back(self):
        from .auth import AuthPage
        back_button = self.find_element(RegisterLocators.BACK_BUTTON)
        back_button.click()
        auth = AuthPage(self.driver)
        assert auth.is_loaded()
        return auth

    def is_loaded(self) -> bool:
        try:
            elem = self.find_element(RegisterLocators.REGISTER_BUTTON)
            return elem.is_displayed()
        except TimeoutException:
            return False
