import pytest

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from ui.pages.register import RegPage
from ui.base_case import BaseCase
import time

class TestRegisterErrors(BaseCase):
    authorize = False

    def test_opening_reg_page(self):
        self.reg_page.open()

    WRONG_LOGIN_WITH_NUMBERS = '123'
    EMPTY_PASS = 'empty_pass'
    EMPTY_EMAIL = 'empty_email'
    SHORT_PASS = 'short'
    ONLY_NUMBERS_PASS = '12345678'
    ONLY_LETTERS_PASS = 'abcdefgh'
    REAL_USER_LOGIN = 'MarkTven'
    TEST_USER_LOGIN = 'test@test.ru'
    TEST_USER_PASS = 'passwordAZAZA123'

    def test_wrong_username(self):
        self.reg_page.open()

        login_input = self.reg_page.find(self.reg_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, self.WRONG_LOGIN_WITH_NUMBERS)
        
        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, self.EMPTY_PASS)
        
        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.LOGIN_NOTIFICATION)
        
        assert str(notification.text) == 'Введите действительное имя' 

    def test_empty_email(self):
        self.reg_page.open()

        email_input = self.reg_page.find(self.reg_page.locators.EMAIL_INPUT, 10)
        self.reg_page.send_keys(email_input, self.EMPTY_EMAIL)
        self.reg_page.send_keys(email_input, '')

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, '')

        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.EMAIL_NOTIFICATION)
        
        assert str(notification.text) == 'Заполните поле' 
    
    def test_wrong_email(self):
        self.reg_page.open()

        email_input = self.reg_page.find(self.reg_page.locators.EMAIL_INPUT, 10)
        self.reg_page.send_keys(email_input, self.EMPTY_EMAIL)

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, '')

        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.EMAIL_NOTIFICATION)
        
        assert str(notification.text) == 'Введите действительный email' 

    def test_empty_password(self):
        self.reg_page.open()

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, self.EMPTY_PASS)
        self.reg_page.send_keys(password_input, '')
        
        login_input = self.reg_page.find(self.reg_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, '')

        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.PASSWORD_NOTIFICATION)
        
        assert str(notification.text) == 'Заполните поле' 
    
    def test_short_password(self):
        self.reg_page.open()

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, self.SHORT_PASS)
        
        login_input = self.reg_page.find(self.reg_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, '')

        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.PASSWORD_NOTIFICATION)
        
        assert str(notification.text) == 'Не меньше 8-ми символов' 
    
    def test_password_with_only_numbers(self):
        self.reg_page.open()

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, self.ONLY_NUMBERS_PASS)
        
        login_input = self.reg_page.find(self.reg_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, '')

        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.PASSWORD_NOTIFICATION)
        
        assert str(notification.text) == 'Необходимы цифры и латинские буквы' 
    
    def test_password_with_only_letters(self):
        self.reg_page.open()

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, self.ONLY_LETTERS_PASS)
        
        login_input = self.reg_page.find(self.reg_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, '')

        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.PASSWORD_NOTIFICATION)
        
        assert str(notification.text) == 'Необходимы цифры и латинские буквы' 

    def test_wrong_second_password(self):
        self.reg_page.open()

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, self.EMPTY_PASS)

        password_copy_input = self.reg_page.find(self.reg_page.locators.PASSWORD_COPY_INPUT, 10)
        self.reg_page.send_keys(password_copy_input, self.EMPTY_PASS)
        self.reg_page.send_keys(password_copy_input, '')
        
        login_input = self.reg_page.find(self.reg_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, '')

        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.PASSWORD_COPY_NOTIFICATION)
        
        assert str(notification.text) == 'Пароли не совпадают' 

    def test_exist_user(self, request: FixtureRequest):
        self.reg_page.open()

        email, password = request.getfixturevalue('credentials')
        
        login_input = self.reg_page.find(self.reg_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, self.REAL_USER_LOGIN)

        email_input = self.reg_page.find(self.reg_page.locators.EMAIL_INPUT, 10)
        self.reg_page.send_keys(email_input, email)

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, password)

        password_copy_input = self.reg_page.find(self.reg_page.locators.PASSWORD_COPY_INPUT, 10)
        self.reg_page.send_keys(password_copy_input, password)

        self.reg_page.click((self.reg_page.locators.REGISTER_BUTTON), 10)

        notification = self.reg_page.wait_visability_of_elem(self.reg_page.locators.USER_EXISTS_NOTIFICATION)
        
        assert str(notification.text) == 'Такой пользователь уже существует' 

    def test_new_user(self):
        self.reg_page.open()

        username = 'TestUser'

        login_input = self.reg_page.find(self.reg_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, username)

        email_input = self.reg_page.find(self.reg_page.locators.EMAIL_INPUT, 10)
        self.reg_page.send_keys(email_input, str(time.time()) + self.TEST_USER_LOGIN)

        password_input = self.reg_page.find(self.reg_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, self.TEST_USER_PASS)

        password_copy_input = self.reg_page.find(self.reg_page.locators.PASSWORD_COPY_INPUT, 10)
        self.reg_page.send_keys(password_copy_input, self.TEST_USER_PASS)

        self.reg_page.click((self.reg_page.locators.REGISTER_BUTTON), 10)

        self.reg_page.is_opened(self.base_page.url)

        header_name = self.reg_page.find(self.base_page.locators.BUTTON_PROFILE_1, 10)
        assert str(header_name.text) == username


