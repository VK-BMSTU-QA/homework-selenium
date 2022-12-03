import queue
import unittest
import subprocess
import os
from pageobjects.pages.signup import SignUpPage
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        print("done")
        
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(60)
        self.signUpPage = SignUpPage(self.driver)

    def tearDown(self):
        self.driver.close()
