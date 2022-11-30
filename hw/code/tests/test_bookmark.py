from pageobjects.pages.bookmark import BookmarkPage
from tests.base_test_case import BaseTestCase
import time


class BookmarkTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = BookmarkPage(self.driver)

    def test_movie(self):
        self.page.open()
        img = self.page.movie_img
        if img == None:
            print('log: no movies in bookmark. Fill it with films first to test')
            return
        img.click()
        self.assertTrue(
            'https://park-akino.ru/movies/' in self.page.driver.current_url,
            'Movie test'
        )

    def test_remove_movie(self):
        self.page.open()
        oldlen = len(self.page.movie_cards)
        btn = self.page.remove_movie_btn
        if btn == None:
            print('log: no movies in bookmark. Fill it with films first to test')
            return
        btn.click()
        el = self.page.notify_msg
        self.assertTrue(
            el != None and
            el.text == 'Фильм удалён' and
            oldlen == len(self.page.movie_cards) + 1,
            'Remove movie test')

    def test_name_change(self):
        self.page.open()
        oldtitle = self.page.bookmark_title.get_attribute("value")
        tmp = ' tested'
        self.page.change_title(tmp)
        self.assertEqual(
            oldtitle + tmp,
            self.page.bookmark_title.get_attribute("value"),
            'Bookmark title change'
        )

    def test_remove_bookmark_cancel(self):
        self.page.open()
        self.page.remove_bookmark_btn.click()
        self.page.popup_cancel_btn.click()
        self.assertTrue(self.page.popup == None, 'Remove bookmark cancel test')

    def test_remove_bookmark_sub(self):
        self.page.open()
        oldurl = self.page.driver.current_url
        self.page.remove_bookmark_btn.click()
        self.page.popup_sub_btn.click()
        self.page.bookmark_elements[0].click()
        self.assertTrue(
            oldurl != self.page.driver.current_url,
            'Remove bookmark submit test'
        )
