from pageobjects.pages.desk import DeskPage
from pageobjects.components.modal_list import ModalList
from pageobjects.components.header import Header
from pageobjects.components.desk import Desk
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
    
    def test_create_column(self):
        self.open_desk()
        title = "test_title"
        self.page.create_list(title)
        self.page.check_new_list(title)
    
    def test_close_popup_icon(self):
        self.open_desk()
        self.page.btn_new_list.click()
        ModalList.create(self.driver)
        self.page.popup_new_list_close_icon.click()
        self.assertEqual(self.page.popup_new_list_check_active, False)

    def test_close_popup_btn(self):
        self.open_desk()
        self.page.btn_new_list.click()
        ModalList.create(self.driver)
        self.page.popup_new_list_close_btn.click()
        self.assertEqual(self.page.popup_new_list_check_active, False)
    
    def test_create_card(self):
        self.create_list("title")
        self.page.btn_new_card.click()
        ModalList.create(self.driver)
        

        
