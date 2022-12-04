from pageobjects.pages.signup import SignUpPage
from pageobjects.components.header import Header
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data, urls, cookie_name, signup_errors
import time

class SignUpTest(BaseTestCase): # Иванов Виктор Михайлович
    def setUp(self):
        super().setUp()
        self.page = SignUpPage(self.driver)

    # def test_signup(self): # Иванов Виктор Михайлович
    #     self.page.open()
    #     self.page.signup(time.time(), authorization_data["password"], authorization_data["password"])
    #     Header.create(self.driver)
    #     all_cookies=self.driver.get_cookies()
    #     is_cookie_set = False
    #     for cookie in all_cookies:
    #         if cookie['name'] == cookie_name:
    #             is_cookie_set = True
    #             break
    #     self.assertEqual(True, is_cookie_set)
    #     self.assertEqual(urls["base_url"], self.driver.current_url)

    # def test_signup_empty_error(self): # Иванов Виктор Михайлович
    #     self.page.open()
    #     self.page.btn_enter.click()
    
    #     self.assertEqual(signup_errors["empty_enter"], self.page.get_error())

    # def test_signup_already_exist(self): # Иванов Виктор Михайлович
    #     self.page.open()
    #     self.page.signup(authorization_data["login"], authorization_data["password"], authorization_data["password"])

    #     self.assertEqual(signup_errors["already_exist"], self.page.get_error())

    # def test_signup_repeat_pass(self): # Иванов Виктор Михайлович
    #     self.page.open()
    #     self.page.signup(time.time(), authorization_data["password"], authorization_data["password"] + "1")

    #     self.assertEqual(signup_errors["repeat_pass"], self.page.get_error())

    # def tearDown(self):
    #     super().tearDown()
