from pageobjects.components.header import Header
from pageobjects.pages.base import BasePage

from tests.base_test_case import BaseTestCase


class NavbarTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = (self.driver)


    def test_click(self):
            self.page.open()

            self.page.btn_login.click()
            self.assertEqual("https://park-akino.ru/login", self.driver.current_url)

            self.page.btn_logo.click()
            self.assertEqual("https://park-akino.ru/", self.driver.current_url)
            self.page.btn_collections.click()
            self.assertEqual("https://park-akino.ru/collections", self.driver.current_url)

            self.assertEqual(self.page.btn_collections.value_of_css_property('color'), "rgba(171, 35, 255, 1)")

            self.page.btn_genres.click()
            self.assertEqual(self.page.btn_genres.value_of_css_property('color'), "rgba(171, 35, 255, 1)")

            self.assertEqual("https://park-akino.ru/genres", self.driver.current_url)

            self.page.btn_premiers.click()
            self.assertEqual(self.page.btn_premiers.value_of_css_property('color'), "rgba(171, 35, 255, 1)")

            self.assertEqual("https://park-akino.ru/premiers", self.driver.current_url)

            self.page.btn_search.click()
            self.assertEqual("https://park-akino.ru/search/", self.driver.current_url)

        def test_profile(self):
            self.page.open()
            self.page.login(authorization_data['login'], authorization_data['password'])
            ActionChains(self.driver).move_to_element(self.page.btn_profile).perform()
            self.page.btn_profile_submenu.click()

            self.assertEqual("https://park-akino.ru/profile/58", self.driver.current_url)

            self.page.btn_logout_submenu.click()
            self.assertEqual("https://park-akino.ru/profile/58", self.driver.current_url)