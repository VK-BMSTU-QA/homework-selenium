import time
from typing import List

from .base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .locators.header import HeaderLocators
from .locators.header import MenuLocators
from .locators.draft import DraftLocators
from .locators.send import SendLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class Draft:
    def __init__(self, address='', theme='', text=''):
        self.address = address
        self.theme = theme
        self.text = text

class DraftPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, add_url="draft")

    def is_redirected(self, url) -> bool:
        return self.is_url_endswith(url)

    def go_to_index(self):
        logo_button = self.find_element(HeaderLocators.LOGO_BUTTON)
        logo_button.click()
        assert self.is_redirected('')

    def list_count(self) -> int:
        items = self.find_elements(DraftLocators.DRAFTS, soft=True)
        return len(items)

    def delete_all(self) -> int:
        items = self.find_elements(DraftLocators.DRAFTS, soft=True)
        action_chains = ActionChains(self.driver)
        for item in items:
            action_chains.context_click(item).perform()
            delete_button = self.find_element(DraftLocators.DELETE_BUTTON)
            delete_button.click()
            time.sleep(0.5)
        assert self.list_count() == 0

    def fill_draft_form(self, draft):
        address_input = self.find_element(SendLocators.ADDRESS_INPUT)
        address_input.clear()
        address_input.send_keys(draft.address)

        theme_input = self.find_element(SendLocators.THEME_INPUT)
        theme_input.clear()
        theme_input.send_keys(draft.theme)

        text_input = self.find_element(SendLocators.TEXT_INPUT)
        text_input.clear()
        text_input.send_keys(draft.text)

    def create_draft(self, draft, cancel=False, attach=''):
        income_button = self.find_element(MenuLocators.INCOME_BUTTON)
        income_button.click()
        send_button = self.find_element(MenuLocators.SEND_BUTTON)
        send_button.click()

        self.fill_draft_form(draft)

        # if attach != '':
        #     attach_input = self.find_element(SendLocators.FILE_INPUT)
        #     attach_input.send_keys(attach)

        menu_draft_button = self.find_element(SendLocators.MENU_INCOME_BUTTON)
        menu_draft_button.click()

        if cancel:
            draft_cancel_button = self.find_element(SendLocators.POPUP_DRAFT_CANCEL_BUTTON)
            draft_cancel_button.click()
        else:
            draft_save_button = self.find_element(SendLocators.POPUP_DRAFT_SAVE_BUTTON)
            draft_save_button.click()
        time.sleep(1)
        self.go_to_site()

    def list(self) -> List[WebElement]:
        items = self.find_elements(DraftLocators.DRAFTS, soft=True)
        return items

    def open_draft(self, index):
        drafts_list = self.list()
        assert len(drafts_list) > index
        item = drafts_list[index]
        item.click()

    def get_draft_value(self) -> Draft:
        address_input = self.find_element(SendLocators.ADDRESS_INPUT).get_attribute('value')
        theme_input = self.find_element(SendLocators.THEME_INPUT).get_attribute('value')
        text_input = self.find_element(SendLocators.TEXT_INPUT).get_attribute('value')

        return Draft(address_input, theme_input, text_input)

    def update_draft(self, draft):
        self.fill_draft_form(draft)

        draft_save_button = self.find_element(DraftLocators.SAVE_BUTTON)
        draft_save_button.click()


