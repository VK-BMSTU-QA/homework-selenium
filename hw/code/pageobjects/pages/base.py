from selenium.webdriver.common.by import By

from pageobjects.base.page import Page
from pageobjects.components.modal_desk import ModalDesk

class BasePage(Page):

    @property
    def btn_new_desk(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDeskButtonUnic")

    @property
    def popup_new_desk(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk")

    @property
    def popup_new_desk_check_active(self):
        if "active" in self.popup_new_desk.get_attribute("class"):
            return True
        return False
    
    @property
    def title_input(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk__settings_input")

    @property
    def desc_input(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk__settings_textarea")
    
    @property
    def create_desk_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk__settings_save")

    @property
    def get_desk(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="desk")

    @property
    def desk_title(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="desk__title")
    
    @property
    def desk_description(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="desk__description")

    @property
    def popup_new_desk_close_icon(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk__close")
    
    @property
    def popup_new_desk_close_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk__settings_cancel")
    
    def get_error(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__block_error_text").text

    def create_desk(self, title, description):
        self.btn_new_desk.click()
        ModalDesk.create(self.driver)
        self.title_input.send_keys(title)
        self.desc_input.send_keys(description)
        self.create_desk_btn.click()

    def check_new_desk(self, title, description):
        if self.desk_title.text == title and self.desk_description.text == description:
            return True
        return False

        