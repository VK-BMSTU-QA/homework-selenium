from pageobjects.pages.signup import SignUpPage
from tests.base_test_case import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
import time

errors = {
    "username": "Количество символов больше 30 или введены небуквенные символы!",
    "email": "Неправильный email!",
    "short_password": "Пароль должен содержать хотя бы 8 символов!",
    "no_digit_password": "Пароль должен содержать хотя бы 1 цифру!",
    "no_letter_password": "Пароль должен содержать хотя бы 1 латинскую букву!",
    "password_match": "Пароли не совпадают!",
    "empty_field": "Заполните поле!",
}

class SignUpTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = SignUpPage(self.driver)


    # submit button
    def test_signup(self):
        self.page.open()
        self.page.signup("username", str(time.time()) + "@vk.ru", "1234abcd", "1234abcd")

        while (self.driver.current_url != "https://park-akino.ru/collections"):
            None
        self.assertEqual("https://park-akino.ru/collections", self.driver.current_url)

    def test_negative_signup(self):
        self.page.open()
        self.page.signup("username", str(time.time()) + ".vk@ru", "1234abcd", "1234abcd")
        self.assertNotEqual("https://park-akino.ru/collections", self.driver.current_url)

    def test_negative_some_empty_signup(self):
        self.page.open()
        self.page.signup("", "", "1234abcd", "1234abcd")
        self.assertEqual(errors["empty_field"], self.page.get_error_username())
        self.assertEqual(errors["empty_field"], self.page.get_error_email())

    def test_negative_all_empty_signup(self):
        self.page.open()
        self.page.signup("", "", "", "")
        self.assertEqual(errors["empty_field"], self.page.get_error_username())
        self.assertEqual(errors["empty_field"], self.page.get_error_email())
        self.assertEqual(errors["empty_field"], self.page.get_error_password())
        self.assertEqual(errors["empty_field"], self.page.get_error_password_repeate())

    # Username
    def test_signup_fill_username(self):
        self.page.open()
        test_usernames = ["uя", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
        for i in test_usernames:
            self.page.fill_username(i)
            self.assertNotEqual(errors["username"], self.page.get_error_username())

    def test_negative_signup_fill_username(self):
        self.page.open()
        test_usernames = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "1viktor3", "#@&?*"]
        for i in test_usernames:
            self.page.fill_username(i)
            self.assertEqual(errors["username"], self.page.get_error_username())

    def test_negative_signup_fill_empty_username(self):
        self.page.open()
        self.page.fill_username('')
        self.assertEqual(errors["empty_field"], self.page.get_error_username())

    # Email
    def test_signup_fill_email(self):
        self.page.open()
        test_emails = ["a@2.r", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaa@a.ru"]
        for i in test_emails:
            self.page.fill_email(i)
            self.assertNotEqual(errors["email"], self.page.get_error_email())

    def test_negative_signup_fill_email(self):
        self.page.open()
        test_emails = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaа@2.ru", "aa.a@ru"]
        for i in test_emails:
            self.page.fill_email(i)
            self.assertEqual(errors["email"], self.page.get_error_email())

    def test_negative_signup_fill_empty_email(self):
        self.page.open()
        self.page.fill_email('')
        self.assertEqual(errors["empty_field"], self.page.get_error_email())

    # Password
    def test_signup_fill_password(self):
        self.page.open()
        self.page.fill_password("1234abcd")
        self.assertNotEqual(errors["short_password"], self.page.get_error_password())

    def test_negative_signup_fill_password(self):
        self.page.open()
        # test_passwords = ["1234abc", "12345aaaaa12345123456","12345678","qwertyui"]
        test_passwords = ["1234abc"]
        for i in test_passwords:
            self.page.fill_password(i)
            self.assertEqual(errors["short_password"], self.page.get_error_password())
   
    def test_signup_fill_password(self):
        self.page.open()
        self.page.fill_password("12345678")
        self.assertEqual(errors["no_letter_password"], self.page.get_error_password())
   
    def test_signup_fill_password(self):
        self.page.open()
        self.page.fill_password("qwertyui")
        self.assertEqual(errors["no_digit_password"], self.page.get_error_password())

    def test_negative_signup_fill_empty_password(self):
        self.page.open()
        self.page.fill_password("")
        self.assertEqual(errors["empty_field"], self.page.get_error_password())


    def test_negative_signup_fill_empty_password_repeat(self):
        self.page.open()
        self.page.fill_password_repeat("")
        self.assertEqual(errors["empty_field"], self.page.get_error_password_repeate())





    # def test_signup_empty_error(self):
    #     self.page.open()
    #     self.page.btn_enter.click()
    
    #     self.assertEqual(errors["empty_enter"], self.page.get_error())

    # def test_signup_already_exist(self):
    #     self.page.open()
    #     self.page.signup(authorization_data["login"], authorization_data["password"], authorization_data["password"])

    #     self.assertEqual(errors["already_exist"], self.page.get_error())

    # def test_signup_repeat_pass(self):
    #     self.page.open()
    #     self.page.signup(time.time(), authorization_data["password"], authorization_data["password"] + "1")

    #     self.assertEqual(errors["repeat_pass"], self.page.get_error())

    # def tearDown(self):
    #     super().tearDown()
