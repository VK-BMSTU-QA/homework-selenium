from pageobjects.pages.desk import DeskPage
from pageobjects.components.modal_list import ModalList
from pageobjects.components.header import Header
from pageobjects.components.desk import Desk
from pageobjects.components.card import Card
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data,urls,cookie_name,create_desc_errors
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
        self.driver.refresh()
        self.page.open_new_card()
        Card.create(self.driver)

    # def test_create_card(self):
    #     title = "test_title"
    #     self.create_card(title)
    
    # def test_create_column(self):
    #     title = "test_title"
    #     self.create_list(title)
    
    # def test_close_popup_icon(self):
    #     self.open_desk()
    #     self.page.btn_new_list.click()
    #     ModalList.create(self.driver)
    #     self.page.popup_new_list_close_icon.click()
    #     self.assertEqual(self.page.popup_new_list_check_active, False)

    # def test_close_popup_btn(self):
    #     self.open_desk()
    #     self.page.btn_new_list.click()
    #     ModalList.create(self.driver)
    #     self.page.popup_new_list_close_btn.click()
    #     self.assertEqual(self.page.popup_new_list_check_active, False)
    
    # def test_close_popup_icon_card(self):
    #     self.create_list("title")
    #     self.page.btn_new_card.click()
    #     ModalList.create(self.driver)
    #     self.page.popup_new_list_close_btn.click()
    #     self.assertEqual(self.page.popup_new_list_check_active, False)

    # def test_close_popup_btn_card(self):
    #     self.create_list("title")
    #     self.page.btn_new_card.click()
    #     ModalList.create(self.driver)
    #     self.page.popup_new_list_close_icon.click()
    #     self.assertEqual(self.page.popup_new_list_check_active, False)

    def test_save_card_title(self):
        title = "Тест названия карточки"
        self.open_card()
        self.page.task_title.send_keys(title)
        Card.create(self.driver)
        self.page.click_header()
        title = "test" + title
        self.page.wait_texarea_value(title)
        
        self.reload_card()
        self.assertEqual(self.page.task_title.text, title)




        
