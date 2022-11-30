from urllib.parse import urljoin
import selenium.webdriver
from selenium.webdriver.common.by import By


class Page(object):
    BASE_URL = 'https://park-akino.ru/'

    def __init__(self, driver):
        self.driver = driver 

    def open(self, path):
        url = urljoin(self.BASE_URL, path)
        self.driver.get(url)
        self.driver.maximize_window()
    