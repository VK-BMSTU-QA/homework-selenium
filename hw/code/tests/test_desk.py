from pageobjects.pages.desk import DeskPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.components.modal_list import ModalList
from pageobjects.components.header import Header
import os
from pageobjects.components.desk import Desk
from pageobjects.components.card import Card
from tests.base_test_case import BaseTestCase
from selenium.webdriver.common.keys import Keys
from utils.constants import authorization_data,urls,cookie_name,create_desc_errors
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time

class DeskTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = DeskPage(self.driver)

    def open_desk(self):
        self.signUpPage.open()
        self.signUpPage.signup_new_user()
        Header.create(self.driver)
        self.basePage.create_desk("title", "description")
        Desk.create(self.driver)
        self.basePage.get_desk.click()
    
    def create_list(self, title):
        self.open_desk()
        self.page.create_list(title)
        self.page.check_new_list(title)

    def create_card(self, title):
        self.create_list(title)
        self.page.create_card(title)
        self.page.check_new_card(title)

    def open_card(self):
        self.create_card('test')
        self.page.open_new_card()
        Card.create(self.driver)

    def reload_card(self):
        self.page.task_close.click()
        self.page.open_new_card()
        Card.create(self.driver)
    
    def upload_file(self, filename):
        self.page.upload_input.send_keys(os.getcwd()+'/' + filename)
    
    def add_comment(self, comment):
        self.open_card()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.page.comment_area().send_keys(comment)
        self.page.comment_area().send_keys(Keys.ENTER)

    def test_create_card(self): # Иванов Виктор Михайлович
        title = "test_title"
        self.create_card(title)
    
    def test_create_column(self): # Иванов Виктор Михайлович
        title = "test_title"
        self.create_list(title)
    
    def test_close_popup_icon(self): # Иванов Виктор Михайлович
        self.open_desk()
        self.page.btn_new_list.click()
        ModalList.create(self.driver)
        self.page.popup_new_list_close_icon.click()
        self.assertEqual(self.page.popup_new_list_check_active, False)

    def test_close_popup_btn(self): # Найденов Александр Валентинович
        self.open_desk()
        self.page.btn_new_list.click()
        ModalList.create(self.driver)
        self.page.popup_new_list_close_btn.click()
        self.assertEqual(self.page.popup_new_list_check_active, False)
    
    def test_close_popup_icon_card(self): # Найденов Александр Валентинович
        self.create_list("title")
        self.page.btn_new_card.click()
        ModalList.create(self.driver)
        self.page.popup_new_list_close_btn.click()
        self.assertEqual(self.page.popup_new_list_check_active, False)

    def test_close_popup_btn_card(self): # Найденов Александр Валентинович
        self.create_list("title")
        self.page.btn_new_card.click()
        ModalList.create(self.driver)
        self.page.popup_new_list_close_icon.click()
        self.assertEqual(self.page.popup_new_list_check_active, False)

    def test_save_card_title(self): # Иванов Виктор Михайлович
        title = "Тест названия карточки"
        self.open_card()
        try:
            self.page.task_title().click()
            self.page.task_title().send_keys(title)
        except:
            self.page.task_title().click()
            self.page.task_title().send_keys(title)
        self.page.wait_texarea_value()
        self.page.click_header()
        self.page.wait_texarea_value()
        
        self.reload_card()

        self.page.wait_texarea_value()
        self.assertEqual(self.page.task_title().text, "test" + title)

    def test_add_user(self): # Найденов Александр Валентинович
        self.open_card()
        a = ActionChains(self.driver)
        a.move_to_element(self.page.btn_add_user()).perform()

        self.page.btn_user().click()
        
        a.move_to_element(self.page.btn_delete_user()).perform()

        self.assertIsNotNone(self.page.popover_username())

        self.page.btn_delete_user().click()

    
    def test_important_task(self): # Иванов Виктор Михайлович
        self.open_card()

        try:
            self.page.not_important_btn().click()
            self.assertIsNotNone(self.page.important_block())
        except:
            self.page.not_important_btn().click()
            self.assertIsNotNone(self.page.important_block())

        self.page.important_btn().click()
        self.assertIsNotNone(self.page.not_important_btn())

    def test_check_list(self): # Найденов Александр Валентинович
        self.open_card()

        self.page.add_checklist()
        self.assertIsNotNone(self.page.checklist())

        self.page.checklist_delete()

        WebDriverWait(self.driver, 5).until_not(EC.presence_of_element_located((By.CLASS_NAME, "taskBlock__checklist")))
    
    def test_check_list_item(self): # Иванов Виктор Михайлович
        self.open_card()
        self.page.add_checklist()

        self.page.add_checklist_item()
        self.assertIsNotNone(self.page.checklist_item())

    def test_url_conntect(self): # Найденов Александр Валентинович
        self.open_card()
        self.page.url_copy_btn.click()
        self.assertEqual(self.page.url_input.get_attribute('value'), pyperclip.paste())

    def test_save_card_decrtiption(self): # Найденов Александр Валентинович
        desc = "Тест описания"
        self.open_card()
        try:
            self.page.task_desctiption().click()
            self.page.task_desctiption().send_keys(desc)
        except:
            self.page.task_desctiption().click()
            self.page.task_desctiption().send_keys(desc)
        self.page.wait_desc_value()
        self.page.click_header()
        self.page.wait_desc_value()
        
        self.reload_card()

        self.page.wait_desc_value()
        self.assertEqual(self.page.task_desctiption().text, desc)

    def test_upload_file(self): # Иванов Виктор Михайлович
        self.open_card()
        filename = 'runner_tests.sh'
        self.upload_file(filename)
        self.assertEqual(self.page.attachment_name[0].text, filename)
    
    def test_delete_file(self): # Иванов Виктор Михайлович
        self.open_card()
        filename = 'runner_tests.sh'
        self.upload_file(filename)
        self.page.delete_file.click()
        WebDriverWait(self.driver, 5).until_not(EC.presence_of_element_located((By.CLASS_NAME, "taskBlock__attachment-delete")))
        self.assertEqual(len(self.page.attachment_name), 0)

    def test_add_comment(self): # Найденов Александр Валентинович
        comment = "test comment"
        self.add_comment(comment)
        self.assertEqual(self.page.comment_text[0].text, comment)
        

    def test_update_comment(self): # Найденов Александр Валентинович
        comment = "test comment"
        self.add_comment(comment)
        self.assertEqual(self.page.comment_text[0].text, comment)
        self.page.comment_text[0].send_keys(comment)
        self.page.comment_text[0].send_keys(Keys.ENTER)
        self.assertEqual(self.page.comment_text[0].text, comment+comment)
    
    def test_delete_comment(self): # Найденов Александр Валентинович
        comment = "test comment"
        self.add_comment(comment)
        self.assertEqual(self.page.comment_text[0].text, comment)

        self.page.comment_delete.click()
        WebDriverWait(self.driver, 5).until_not(EC.presence_of_element_located((By.CLASS_NAME, "taskBlock__comment-text-delete")))
        self.assertEqual(len(self.page.comment_text), 0)
