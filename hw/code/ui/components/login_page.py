from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths

class LoginPage(BaseComponent):

    locators = locators.LoginLocators()
    PATH = paths.LOGIN

    def login(self, phone, code):
        phone_input = self.find(self.locators.PHONE_INPUT)
        self.send_keys_elem(phone_input, phone)
        self.click((self.locators.LOGIN_BUTTON))
        code_input = self.find(self.locators.CODE_INPUT)
        self.send_keys_elem(code_input, code)
        self.click((self.locators.CONFIRM_CODE_BUTTON))
        assert self.is_visible(self.locators.PROFILE_BUTTON)
