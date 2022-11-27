from pageobjects.pages.genres import GenresPage
from tests.base_test_case import BaseTestCase

class GenresTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = GenresPage(self.driver)

    def test_num_cards(self):
        self.page.open('action')
        tmp = self.page.movie_cards
        self.assertFalse(len(tmp) == 0, 'Amount of movie cards is greater than zero')
    
    def test_valid_link(self):
        self.page.open('action')
        self.page.movie_img.click()
        print(self.page.driver.current_url)
        self.assertTrue('https://park-akino.ru/movies/' in self.page.driver.current_url, 'Correct URL after redirect')
