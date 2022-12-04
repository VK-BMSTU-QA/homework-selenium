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

    def task_title(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__title-input")))

    def btn_add_user(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__add-user")))

    def btn_user(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__add-user-block")))

    def btn_delete_user(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".taskBlock__img-block:not(.taskBlock__add-user)")))

    def popover_username(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__img-popover")))

    def important_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__important-task")))

    def not_important_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".taskBlock__not-important-task")))

    def important_block(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "active-tasks__icon-block")))
    
    def add_checklist(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.taskBlock__button-addCheck"))).click()

    def add_checklist_item(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__button-active"))).click()
        except:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__button-active"))).click()

    def checklist(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__checklist")))

    def checklist_item(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__checklist-item-text")))

    def checklist_delete(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__checklist-delete"))).click()

    @property
    def task_close(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="taskBlock__close")

    def wait_texarea_value(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'taskBlock__title-input')))

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

    @property
    def url_input(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[8]/div[2]/div[3]/div[2]/div/div[3]/div/input')))

    @property
    def url_copy_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "createModal__settings_link_icon_task")))

    @property
    def upload_input(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "taskBlock__attachmentButton-input")))

    @property
    def attachment_name(self):
        return self.driver.find_elements_by_xpath(('//*[@id="root"]/div[8]/div[2]/div[6]/div[2]/div[1]/div/span'))
    
    @property
    def delete_file(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "taskBlock__attachment-delete")))

    def comment_area(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "taskBlock__comment-textarea")))

    @property
    def comment_text(self):
        return self.driver.find_elements_by_xpath(('//*[@id="root"]/div[8]/div[2]/div[9]/div[2]/textarea'))
    
    @property
    def comment_delete(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "taskBlock__comment-text-delete")))

    def task_title(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__title-input")))

    def task_desctiption(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "taskBlock__textarea")))

    def wait_desc_value(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'taskBlock__textarea')))