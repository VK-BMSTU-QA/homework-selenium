from selenium.webdriver.common.by import By

from pageobjects.base.page import Page

class BasePage(Page):

    @property
    def btn_new_desk(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDeskButtonUnic")

    @property
    def popup_new_desk(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk")
    
    @property
    def title_input(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk__settings_input")

    @property
    def desc_input(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk__settings_textarea")
    
    @property
    def create_desk_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="createDesk__settings_save")

    def create_desk(self, title, description):
        self.title_input.send_keys(title)
        self.desc_input.send_keys(description)
        self.create_desk_btn.click()

        