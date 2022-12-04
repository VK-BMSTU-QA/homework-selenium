from selenium.webdriver.common.by import By
from pageobjects.base.page import Page
from pageobjects.components.modal_list import ModalList

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    def click_header(self):
        self.driver.find_element(by=By.CLASS_NAME, value="taskBlock_header").click()

    @property
    def card_title(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="desk__task-text")

    @property
    def task_title(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="taskBlock__title-input")

    @property
    def task_close(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="taskBlock__close")

    def wait_texarea_value(self, text):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, f""".taskBlock__title-input[data-info="{text}"]""")))

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

    def open_new_card(self):
        self.driver.find_element(by=By.CLASS_NAME, value="desk__task-text").click()
