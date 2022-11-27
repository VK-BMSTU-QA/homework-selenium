from pageobjects.pages.login import LoginPage
from tests.base_test_case import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = LoginPage(self.driver)

    def test_link_redirect(self):
        self.page.open()
        self.page.go_to_link()
        self.assertEqual("https://github.com/Kislv/", self.driver.current_url)

    def test_GH_image(self):
        self.page.open()
        self.page.go_to_GH()
        # self.assertEqual("https://github.com/Kislv/2022_1_CoDex", self.driver.current_url)
        self.assertEqual("https://park-akino.ru/login", self.driver.current_url)


