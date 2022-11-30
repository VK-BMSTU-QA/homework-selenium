# from pageobjects.pages.login import LoginPage
# from tests.base_test_case import BaseTestCase
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os

# errors = {
#     "email": "Неправильный email!",
#     "short_password": "Пароль должен содержать хотя бы 8 символов!",
#     "no_digit_password": "Пароль должен содержать хотя бы 1 цифру!",
#     "no_letter_password": "Пароль должен содержать хотя бы 1 латинскую букву!",
#     "password_match": "Пароли не совпадают!",
#     "empty_field": "Заполните поле!",
# }

# class LoginTest(BaseTestCase):
#     def setUp(self):
#         super().setUp()
#         self.page = LoginPage(self.driver)

#     # Email
#     def test_login_fill_email(self):
#         self.page.open()
#         test_emails = ["a@2.r", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaa@a.ru"]
#         for i in test_emails:
#             self.page.fill_email(i)
#             self.assertNotEqual(errors["email"], self.page.get_error_email())

#     def test_negative_login_fill_email(self):
#         self.page.open()
#         test_emails = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaа@2.ru", "aa.a@ru"]
#         for i in test_emails:
#             self.page.fill_email(i)
#             self.assertEqual(errors["email"], self.page.get_error_email())

#     def test_negative_login_fill_empty_email(self):
#         self.page.open()
#         self.page.fill_email('')
#         self.assertEqual(errors["empty_field"], self.page.get_error_email())

#     # Password
#     def test_login_fill_password(self):
#         self.page.open()
#         self.page.fill_password("1234abcd")
#         self.assertNotEqual(errors["short_password"], self.page.get_error_password())

#     def test_negative_login_fill_password(self):
#         self.page.open()
#         # test_passwords = ["1234abc", "12345aaaaa12345123456","12345678","qwertyui"]
#         test_passwords = ["1234abc"]
#         for i in test_passwords:
#             self.page.fill_password(i)
#             self.assertEqual(errors["short_password"], self.page.get_error_password())
   
#     def test_login_fill_password(self):
#         self.page.open()
#         self.page.fill_password("12345678")
#         self.assertEqual(errors["no_letter_password"], self.page.get_error_password())
   
#     def test_login_fill_password(self):
#         self.page.open()
#         self.page.fill_password("qwertyui")
#         self.assertEqual(errors["no_digit_password"], self.page.get_error_password())

#     def test_negative_login_fill_empty_password(self):
#         self.page.open()
#         self.page.fill_password("")
#         self.assertEqual(errors["empty_field"], self.page.get_error_password())


#     # submit button
#     def test_login(self):
#         self.page.open()
#         # self.page.login("a@vk.ru", "1234abcd")
#         self.page.login(os.environ.get('AKINO_LOGIN'), os.environ.get('AKINO_PASSWORD'))
#         while (self.driver.current_url != "https://park-akino.ru/collections"):
#             None
#         self.assertEqual("https://park-akino.ru/collections", self.driver.current_url)

#     def test_negative_login(self):
#         self.page.open()
#         self.page.login(str(time.time()) + ".vk@ru", "1234abcd")
#         self.assertNotEqual("https://park-akino.ru/collections", self.driver.current_url)

#     def test_negative_some_empty_login(self):
#         self.page.open()
#         self.page.login("", "1234abcd")
#         self.assertEqual(errors["empty_field"], self.page.get_error_email())

#     def test_negative_all_empty_login(self):
#         self.page.open()
#         self.page.login("", "")
#         self.assertEqual(errors["empty_field"], self.page.get_error_email())
#         self.assertEqual(errors["empty_field"], self.page.get_error_password())
