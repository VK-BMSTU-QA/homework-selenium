from pageobjects.pages.login import LoginPage
from pageobjects.pages.collections import CollectionsPage
from tests.base_test_case import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from selenium.webdriver import ActionChains

class NavbarTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.loginPage = LoginPage(self.driver)
        self.page = CollectionsPage(self.driver)

    def test_navigation_not_auth(self):
        self.page.open()    

        self.page.btn_navbar_collections.click()
        self.assertEqual("https://park-akino.ru/collections", self.driver.current_url)

        self.page.btn_navbar_genres.click()
        self.assertEqual("https://park-akino.ru/genres", self.driver.current_url)

        self.page.btn_navbar_premiers.click()
        self.assertEqual("https://park-akino.ru/premiers", self.driver.current_url)

        self.page.btn_logo.click()
        self.assertEqual("https://park-akino.ru/", self.driver.current_url)

        self.page.btn_navbar_search.click()
        self.assertEqual("https://park-akino.ru/search/", self.driver.current_url)

        self.page.btn_navbar_login.click()
        self.assertEqual("https://park-akino.ru/login?redirect=/search/", self.driver.current_url)

    
    def test_navigation_auth(self):
        self.loginPage.open()    
        self.loginPage.login(os.environ.get('AKINO_LOGIN'), os.environ.get('AKINO_PASSWORD'))

        self.assertEqual(self.page.btn_profile.is_displayed(), True)

        self.page.btn_profile.click()
        self.assertEqual("https://park-akino.ru/profile/115", self.driver.current_url)

        ActionChains(self.driver).move_to_element(self.page.btn_profile).perform()
        self.assertEqual(self.page.btn_profile_submenu.is_displayed(), True)
        self.assertEqual(self.page.btn_logout_submenu.is_displayed(), True)


        self.page.btn_profile_submenu.click()
        self.assertEqual("https://park-akino.ru/profile/115", self.driver.current_url)

        self.page.btn_logout_submenu.click()
        self.assertEqual(self.page.btn_navbar_login.is_displayed(), True)
        
    def test_button_color(self):
        self.page.open()
        
        self.page.btn_navbar_collections.click()
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.visibility_of(self.page.btn_navbar_collections))

        self.assertEqual(self.page.btn_navbar_collections.value_of_css_property('color'), "rgba(171, 35, 255, 1)")

        self.page.btn_navbar_genres.click()
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.visibility_of(self.page.btn_navbar_genres))

        self.assertEqual(self.page.btn_navbar_genres.value_of_css_property('color'), "rgba(171, 35, 255, 1)")

        self.page.btn_navbar_premiers.click()
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.visibility_of(self.page.btn_navbar_premiers))

        self.assertEqual(self.page.btn_navbar_premiers.value_of_css_property('color'), "rgba(171, 35, 255, 1)")
