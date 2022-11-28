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

    @property
    def btn_profile(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="user-block__profile-href")

    @property
    def btn_profile_submenu(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="user-block__submenu__block")

    @property
    def btn_logout_submenu(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="user-block").find_element(by=By.CLASS_NAME, value="user-block__logout-btn")

    @property
    def btn_logo(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="navbar__logo")

    @property
    def btn_navbar_collections(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__menu").find_element(by=By.CLASS_NAME, value="collections")

    @property
    def btn_navbar_genres(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__menu").find_element(by=By.CLASS_NAME, value="genres")
    
    @property
    def btn_navbar_premiers(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__menu").find_element(by=By.CLASS_NAME, value="premiers")
    
    @property
    def btn_navbar_search(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="search__btn")

    @property
    def btn_navbar_login(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="navbar__login-btn")