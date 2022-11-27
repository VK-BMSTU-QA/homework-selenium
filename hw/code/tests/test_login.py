from pageobjects.pages.login import LoginPage
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data
from selenium.webdriver.common.action_chains import ActionChains
import time

errors = {
    "empty_enter": "Логин и пароль должны составлять от 7 до 20 символов",
    "wrong_user": "Пожалуйста, проверьте правильность написания логина и пароля",
}

class LoginTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        
        self.page = LoginPage(self.driver)

    


