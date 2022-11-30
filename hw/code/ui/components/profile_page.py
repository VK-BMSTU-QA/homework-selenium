from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class ProfilePage(BaseComponent):
    locators = locators.ProfileLocators()
    PATH = paths.PROFILE

    def send_new_name(self, name):
        self.send_keys_enter(self.locators.NAME_INPUT, name)
        self.click(self.locators.SAVE_BUTTON)

    def send_new_email(self, email):
        self.send_keys_enter(self.locators.EMAIL_INPUT, email)
        self.click(self.locators.SAVE_BUTTON)
