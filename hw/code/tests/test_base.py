from pageobjects.pages.base import BasePage
from pageobjects.components.header import Header
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data,urls,cookie_name

errors = {
    "empty_enter": "Логин и пароль должны составлять от 7 до 20 символов",
    "wrong_user": "Пожалуйста, проверьте правильность написания логина и пароля",
}

class BaseTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = BasePage(self.driver)

    def test_create_desk(self): 
        self.signUpPage.open()
        self.signUpPage.signup_new_user()
        Header.create(self.driver)
        self.page.btn_new_desk.click()
        self.page.create_desk("title", "desctiption")
    
