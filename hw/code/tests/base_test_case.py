import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTestCase(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--log-level=3')
        
        self.driver = webdriver.Chrome(
            executable_path="chromedriver",
            options=chrome_options
        )

        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(60)

    def tearDown(self):
        self.driver.close()
