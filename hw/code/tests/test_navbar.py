from pageobjects.components.header import Header
from pageobjects.pages.base import BasePage

from tests.base_test_case import BaseTestCase


class NavbarTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = (self.driver)

    def test_navigation(self):
        self.page.open()    

        self.page.btn_collections.click()

        self.assertEqual(self.page.btn_collections_container, 12)

        self.page.btn_collection.click()
        self.assertEqual("https://park-akino.ru/collections/1", self.driver.current_url)

        self.page.btn_genres.click()
        time.sleep(4)
        self.assertEqual(self.page.btn_genres_container, 20)
        self.page.btn_genre.click()
        self.assertEqual("https://park-akino.ru/genres/action", self.driver.current_url)

        self.page.btn_premiers.click()
        self.page.btn_premier.click()
        self.assertEqual("https://park-akino.ru/announced/8", self.driver.current_url)
