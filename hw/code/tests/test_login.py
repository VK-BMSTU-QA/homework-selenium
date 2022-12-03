# Найденов Александр Валентинович
from pageobjects.pages.login import LoginPage
from pageobjects.components.header import Header
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data,urls,cookie_name

errors = {
    "empty_enter": "Логин и пароль должны составлять от 7 до 20 символов",
    "wrong_user": "Пожалуйста, проверьте правильность написания логина и пароля",
}

class LoginTest(BaseTestCase): # Найденов Александр Валентинович
    def setUp(self):
        super().setUp()
        self.page = LoginPage(self.driver)

    # def test_login_empty_error(self): # Найденов Александр Валентинович
    #     self.page.open()
    #     self.page.btn_enter.click()
    
    #     self.assertEqual(errors["empty_enter"], self.page.get_error())

    # def test_login_wrong_user(self): # Найденов Александр Валентинович
    #     self.page.open()
    #     self.page.login(authorization_data["wrong_login"], authorization_data["wrong_password"])

    #     self.assertEqual(errors["wrong_user"], self.page.get_error())
    
    # def test_login(self): # Найденов Александр Валентинович
    #     self.page.open()
    #     self.page.login(authorization_data["login"], authorization_data["password"])
    #     Header.create(self.driver)
    #     all_cookies=self.driver.get_cookies()
    #     is_cookie_set = False
    #     for cookie in all_cookies:
    #         if cookie['name'] == cookie_name:
    #             is_cookie_set = True
    #             break
    #     self.assertEqual(True, is_cookie_set)
    #     self.assertEqual(urls["base_url"], self.driver.current_url)
        
