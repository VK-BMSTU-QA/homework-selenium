from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class RegisterPage(BaseComponent):
    locators = locators.RegisterLocators()
    PATH = paths.REGISTER

    def send_register_data(self, phone, username, email):
        self.send_phone(phone)
        self.send_username(username)
        self.send_email(email)
        self.click(self.locators.REGISTER_BUTTON)

    def send_phone(self, phone):
        self.send_keys(self.locators.PHONE_INPUT, phone)

    def send_email(self, email):
        self.send_keys(self.locators.EMAIL_INPUT, email)

    def send_username(self, username):
        self.send_keys(self.locators.NAME_INPUT, username)
