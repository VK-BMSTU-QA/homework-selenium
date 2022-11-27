import time
import pytest

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from ui.base_case import BaseCase
from ui.pages.login import LoginPage


class TestLoginErrors:
    url = 'https://movie-space.ru/login'

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)
        self.login_page.is_opened(self.url)
        self.login_input = self.login_page.find(self.login_page.locators.LOGIN_INPUT, 10)
        self.password_input = self.login_page.find(self.login_page.locators.PASSWORD_INPUT, 10)

    def test_wrong_email(self):
        self.login_page.send_keys(self.login_input, 'empty_email')
        self.login_page.send_keys(self.password_input, 'empty_pass')
        
        notification = self.login_page.wait_visability_of_elem(self.login_page.locators.LOGIN_NOTIFICATION)
        
        assert str(notification.text) == 'Введите действительный email' 

    def test_empty_email(self):
        self.login_page.send_keys(self.login_input, 'empty_login')
        self.login_page.send_keys(self.login_input, '')

        self.login_page.send_keys(self.password_input, '')

        notification = self.login_page.wait_visability_of_elem(self.login_page.locators.LOGIN_NOTIFICATION)
        
        assert str(notification.text) == 'Заполните поле' 
    
    def test_empty_password(self):
        self.login_page.send_keys(self.password_input, 'empty_pass')
        self.login_page.send_keys(self.password_input, '')
        
        self.login_page.send_keys(self.login_input, '')

        notification = self.login_page.wait_visability_of_elem(self.login_page.locators.PASSWORD_NOTIFICATION)
        
        assert str(notification.text) == 'Заполните поле' 

    def test_user_unexist(self):
        self.login_page.send_keys(self.password_input, 'random_unknown_password_hgyur34rtyrfq34134fjiu')
       
        self.login_page.send_keys(self.login_input, '2356fhnudffjrmcuawerl@gogol.ya')

        self.login_page.click((self.login_page.locators.PASS_LOGIN_CREDS_BUTTON), 10)

        notification = self.login_page.wait_visability_of_elem(self.login_page.locators.USER_DOES_NOT_EXISTS_NOTIFICATION)
        
        assert str(notification.text) == 'Неверный логин или пароль' 



class TestLogin(BaseCase):
    authorize = True

    def test_login(self):

        time.sleep(1)
