from selenium.webdriver.common.by import By
from pageobjects.base.page import Page
from pageobjects.components.modal_list import ModalList

class DeskPage(Page):

    @property
    def btn_new_list(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="desk-newList")

    @property    
    def title_input(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createModal__settings_input")

    @property
    def create_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createModal__settings_save")

    @property
    def list_title(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="desk__column-title")

    @property
    def popup_new_list(self):
        return self.driver.find_elements(by=By.XPATH, value='//*[@id="modalBlock"]/div/div')
    @property
    def popup_new_list_close_icon(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createModal__close")
    
    @property
    def popup_new_list_close_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createModal__settings_cancel")

    @property
    def popup_new_list_check_active(self):
        if len(self.popup_new_list):
            return True
        return False

    @property
    def btn_new_card(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="desk__newButton")
    
    @property
    def card_title(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="desk__task-text")

    def create_list(self, title):
        self.btn_new_list.click()
        ModalList.create(self.driver)
        self.title_input.send_keys(title)
        self.create_btn.click()

    def create_card(self, title):
        self.btn_new_card.click()
        ModalList.create(self.driver)
        self.title_input.send_keys(title)
        self.create_btn.click()
    
    def check_new_list(self, title):
        if self.list_title.text == title:
            return True
        return False
    
    def check_new_card(self, title):
        if self.card_title.text == title:
            return True
        return False
