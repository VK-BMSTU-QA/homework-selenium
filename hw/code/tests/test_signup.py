from pageobjects.pages.signup import SignUpPage
from pageobjects.components.header import Header
from tests.base_test_case import BaseTestCase
from utils.constants import authorization_data
import time

errors = {
    "empty_enter": "Логин и пароль должны составлять от 7 до 20 символов",
    "already_exist": "Пользователь с таким именем уже зарегистрирован",
    "repeat_pass": "Введенные пароли не совпадают",
}

class SignUpTest(BaseTestCase): # Иванов Виктор Михайлович
    def setUp(self):
        super().setUp()
        self.page = SignUpPage(self.driver)

    def test_signup(self): # Иванов Виктор Михайлович
        self.page.open()
        self.page.signup(time.time(), authorization_data["password"], authorization_data["password"])
        Header.create(self.driver)
        self.assertEqual("https://planexa.ru/base", self.driver.current_url)

    def test_signup_empty_error(self): # Иванов Виктор Михайлович
        self.page.open()
        self.page.btn_enter.click()
    
        self.assertEqual(errors["empty_enter"], self.page.get_error())

    def test_signup_already_exist(self): # Иванов Виктор Михайлович
        self.page.open()
        self.page.signup(authorization_data["login"], authorization_data["password"], authorization_data["password"])

        self.assertEqual(errors["already_exist"], self.page.get_error())

    def test_signup_repeat_pass(self): # Иванов Виктор Михайлович
        self.page.open()
        self.page.signup(time.time(), authorization_data["password"], authorization_data["password"] + "1")

        self.assertEqual(errors["repeat_pass"], self.page.get_error())

    def tearDown(self):
        super().tearDown()
