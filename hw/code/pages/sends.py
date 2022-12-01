import threading
import time

from selenium.webdriver import ActionChains

from .base import BasePage

from .locators.send import SendLocators

from .locators.header import MenuLocators


class SendInfo:
    def __init__(self, address='', theme='', text=''):
        self.address = address
        self.theme = theme
        self.text = text


class SendPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, add_url="send")

    def fill_message(self, mes):
        address_input = self.find_element(SendLocators.ADDRESS_INPUT)
        address_input.clear()
        address_input.send_keys(mes.address)

        theme_input = self.find_element(SendLocators.THEME_INPUT)
        theme_input.clear()
        theme_input.send_keys(mes.theme)

        text_input = self.find_element(SendLocators.TEXT_INPUT)
        text_input.clear()
        text_input.send_keys(mes.text)


    def create_message(self, mes, attach=''):
        send_button = self.find_element(MenuLocators.SEND_BUTTON)
        send_button.click()

        self.fill_message(mes)

        send_button = self.find_element(SendLocators.SEND_BUTTON)
        send_button.click()

        time.sleep(1)

    def is_dialog_appear(self) -> bool:
        dialog = self.find_element(SendLocators.EMPTY_THEM_BUTTON)
        return dialog.is_enabled()

    def is_wrong(self) -> bool:
        dialog = self.find_element(SendLocators.ERROR_BOX)
        time.sleep(1)
        return dialog is not None
