from pageobjects.pages.collection import CollectionPage
from tests.base_test_case import BaseTestCase

class CollectionTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = CollectionPage(self.driver)

    def test_num_cards(self):
        self.page.open(1)
        tmp = self.page.movie_cards
        self.assertFalse(len(tmp) == 0, 'Amount of movie cards is greater than zero')
    
    def test_valid_link(self):
        self.page.open(1)
        self.page.movie_img.click()
        print(self.page.driver.current_url)
        self.assertTrue('https://park-akino.ru/movies/' in self.page.driver.current_url, 'Correct URL after redirect')
