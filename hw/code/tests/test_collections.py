from pageobjects.pages.collections import CollectionsPage
from tests.base_test_case import BaseTestCase

class CollectionsTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = CollectionsPage(self.driver)

    def test_correct_navigation(self):
        self.page.open()    

        self.page.btn_navbar_collections.click()
        self.page.btn_collection.click()
        self.assertEqual("https://park-akino.ru/collections/1", self.driver.current_url)


        self.page.btn_navbar_genres.click()
        self.page.btn_genre.click()
        self.assertEqual("https://park-akino.ru/genres/action", self.driver.current_url)

        self.page.btn_navbar_premiers.click()
        self.page.btn_premier.click()
        self.assertEqual("https://park-akino.ru/announced/8", self.driver.current_url)
        
    def test_correct_count(self):
        self.page.open()    

        self.page.btn_navbar_collections.click()
        self.assertEqual(self.page.btn_collections_container, 12)

        self.page.btn_navbar_genres.click()
        self.assertEqual(self.page.btn_genres_container, 20)
