import random
import pytest
import time
from _pytest.fixtures import FixtureRequest

from ui.base_case import BaseCase

class TestProfileContacts(BaseCase):
    authorize = True

    NEW_USERNAME= 'NewUserName'
    SHORT_PASS = 'short'
    EMPTY_PASS = 'empty_pass'
    ONLY_NUMBERS_PASS = '12345678'
    ONLY_LETTERS_PASS = 'abcdefgh'
    NORMAL_PASS = 'abcdefgh123'

    def test_change_username(self):
        self.profile_page.open()

        input_field = self.profile_page.find(self.profile_page.locators.LOGIN_INPUT, 15)

        old_username = input_field.get_attribute('value')

        self.profile_page.send_keys(input_field, self.NEW_USERNAME)

        self.base_page.click(
            self.profile_page.locators.SAVE_BUTTON, 15)

        self.base_page.wait_visability_of_elem(
            self.profile_page.locators.SAVE_NOTIFICATION, 15)

        updated_input_field = self.base_page.find(self.profile_page.locators.BUTTON_PROFILE_1, 15)
        
        assert updated_input_field.text == self.NEW_USERNAME

        self.profile_page.send_keys(input_field, old_username)

        self.base_page.click(
            self.profile_page.locators.SAVE_BUTTON, 15)

        self.base_page.wait_visability_of_elem(
            self.profile_page.locators.SAVE_NOTIFICATION, 15)

        another_updated_input_field = self.base_page.find(self.profile_page.locators.BUTTON_PROFILE_1, 15)

        assert another_updated_input_field.text == old_username


    def test_short_password(self):
        self.profile_page.open()

        password_input = self.reg_page.find(self.profile_page.locators.PASSWORD_INPUT, 10)
        self.reg_page.send_keys(password_input, self.SHORT_PASS)
        
        login_input = self.reg_page.find(self.profile_page.locators.LOGIN_INPUT, 10)
        self.reg_page.send_keys(login_input, '')

        notification = self.profile_page.wait_visability_of_elem(self.profile_page.locators.PASSWORD_NOTIFICATION)
        
        assert str(notification.text) == 'Не меньше 8-ми символов' 
    
    def test_password_with_only_numbers(self):
        self.profile_page.open()

        password_input = self.reg_page.find(self.profile_page.locators.PASSWORD_INPUT, 10)
        self.profile_page.send_keys(password_input, self.ONLY_NUMBERS_PASS)
        
        login_input = self.profile_page.find(self.profile_page.locators.LOGIN_INPUT, 10)
        self.profile_page.send_keys(login_input, '')

        notification = self.profile_page.wait_visability_of_elem(self.profile_page.locators.PASSWORD_NOTIFICATION)
        
        assert str(notification.text) == 'Необходимы цифры и латинские буквы' 
    
    def test_password_with_only_letters(self):
        self.profile_page.open()

        password_input = self.profile_page.find(self.profile_page.locators.PASSWORD_INPUT, 10)
        self.profile_page.send_keys(password_input, self.ONLY_LETTERS_PASS)
        
        login_input = self.profile_page.find(self.profile_page.locators.LOGIN_INPUT, 10)
        self.profile_page.send_keys(login_input, '')

        notification = self.profile_page.wait_visability_of_elem(self.profile_page.locators.PASSWORD_NOTIFICATION)
        
        assert str(notification.text) == 'Необходимы цифры и латинские буквы' 

    def test_wrong_second_password(self):
        self.profile_page.open()

        password_input = self.profile_page.find(self.profile_page.locators.PASSWORD_INPUT, 10)
        self.profile_page.send_keys(password_input, self.NORMAL_PASS)

        password_copy_input = self.profile_page.find(self.profile_page.locators.PASSWORD_COPY_INPUT, 10)
        self.profile_page.send_keys(password_copy_input, self.EMPTY_PASS)
        self.profile_page.send_keys(password_copy_input, '')
        
        self.base_page.click(
            self.profile_page.locators.SAVE_BUTTON, 15)

        notification = self.profile_page.wait_visability_of_elem(self.profile_page.locators.PASSWORD_COPY_NOTIFICATION)
        
        assert str(notification.text) == 'Пароли не совпадают' 

    def test_change_password(self, request: FixtureRequest):
        self.profile_page.open()

        login, password = request.getfixturevalue('credentials')
        
        password_input = self.profile_page.find(self.profile_page.locators.PASSWORD_INPUT, 10)
        self.profile_page.send_keys(password_input, self.NORMAL_PASS)

        password_copy_input = self.profile_page.find(self.profile_page.locators.PASSWORD_COPY_INPUT, 10)
        self.profile_page.send_keys(password_copy_input, self.NORMAL_PASS)
        
        self.profile_page.click(
            self.profile_page.locators.SAVE_BUTTON, 15)

        notification = self.profile_page.wait_visability_of_elem(self.profile_page.locators.SAVE_NOTIFICATION)
        
        assert str(notification.text) == 'Информация обновлена!'

        self.profile_page.move_on_element(self.profile_page.locators.PROFILE_PIC, 3)
        self.profile_page.click(self.profile_page.locators.BUTTON_LOGOUT, 10)

        self.driver.refresh()
        self.profile_page.is_opened('https://movie-space.ru/login')

        self.login_page.login(login, self.NORMAL_PASS)

        self.profile_page.open()

        password_input = self.profile_page.find(self.profile_page.locators.PASSWORD_INPUT, 10)
        self.profile_page.send_keys(password_input, password)

        password_copy_input = self.profile_page.find(self.profile_page.locators.PASSWORD_COPY_INPUT, 10)
        self.profile_page.send_keys(password_copy_input, password)
        
        self.profile_page.click(
            self.profile_page.locators.SAVE_BUTTON, 15)

        notification = self.profile_page.wait_visability_of_elem(self.profile_page.locators.SAVE_NOTIFICATION)
        
        assert str(notification.text) == 'Информация обновлена!'

        self.profile_page.move_on_element(self.profile_page.locators.PROFILE_PIC, 3)
        self.profile_page.click(self.profile_page.locators.BUTTON_LOGOUT, 10)      
        self.driver.refresh()
        self.profile_page.is_opened('https://movie-space.ru/login')

        self.login_page.login(login, password)
