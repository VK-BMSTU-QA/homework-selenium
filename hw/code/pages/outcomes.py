import time
from .base import BasePage

from .locators.outcome import OutcomeLocators
from .locators.send import SendLocators


class OutcomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, add_url="income")

    def list_count(self) -> int:
        items = self.find_elements(OutcomeLocators.OUTCOMES, soft=True)
        return len(items)

    def go_to_look(self, i):
        time.sleep(1)
        items = self.find_elements(OutcomeLocators.OUTCOMES, soft=True)
        print("LEN ITEMS: ", items)
        if i < len(items):
            items[i].click()
        else:
            items[0].click()

    def delete(self):
        item = self.find_element(OutcomeLocators.SETTINGS, soft=True)
        item.click()
        del_but = self.find_element(OutcomeLocators.REMOVE, soft=True)
        del_but.click()

    def is_redirected(self, url) -> bool:
        return self.is_url_endswith(url)

    def reply(self):
        item = self.find_element(OutcomeLocators.REMAIL, soft=True)
        item.click()

    def forward(self):
        item = self.find_element(OutcomeLocators.FORWARD, soft=True)
        item.click()


    def get_theme(self):
        theme = self.find_element(SendLocators.THEME_INPUT, soft=True)
        return theme.get_attribute("value")

    def get_address(self):
        theme = self.find_element(SendLocators.ADDRESS_INPUT, soft=True)
        return theme.get_attribute("value")
