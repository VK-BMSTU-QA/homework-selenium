import threading
import time

from selenium.webdriver import ActionChains

from .base import BasePage
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from locators.auth_reg import AuthLocators
from .locators.send import SendLocators
from hw.code.pages.locators.header import HeaderLocators


class SendPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, add_url="send")

