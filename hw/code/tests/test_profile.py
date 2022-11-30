from pageobjects.pages.profile import ProfilePage
from pageobjects.pages.login import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from tests.base_test_case import BaseTestCase


class ProfileTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.open()
        self.loginPage.login(os.environ.get('AKINO_LOGIN'), os.environ.get('AKINO_PASSWORD'))
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of(self.page.btn_profile))
        self.page.btn_profile.click()

    def test_profile_settings(self):
        self.page.btn_change.click()

        self.assertEqual(self.page.btn_save_name.is_displayed(), True)
        self.assertEqual(self.page.btn_close_settings.is_displayed(), True)

        self.page.btn_close_settings.click()
        self.assertEqual(self.page.btn_change.is_displayed(), True)

        self.page.btn_change.click()
        self.page.btn_save_name.click()
        self.assertEqual(self.page.error_text, "Заполните поле!")

    def test_change_name(self):
        self.page.btn_change.click()
        newName = "kostya"
        self.page.input_name.send_keys(newName)
        self.page.btn_save_name.click()
        self.assertEqual(self.page.name.text, newName)

    def test_bookmark_click(self):
        self.page.btn_single_bookmark.click()
        self.assertTrue('https://park-akino.ru/bookmarks/' in self.page.driver.current_url)

    def test_film_redirect(self):
        self.page.btn_movie_poster.click()
        self.assertTrue('https://park-akino.ru/movies/' in self.page.driver.current_url)

    def test_popup_interaction(self):
        self.page.btn_popup_open.click()
        self.assertEqual(self.page.popup_container.is_displayed(), True)

        self.page.btn_create_bookmark.click()
        self.assertEqual(self.page.popup_container.is_displayed(), True)

        self.page.btn_popup_close.click()
        self.assertEqual(self.page.popup_container.is_displayed(), True)

    def test_popup_create_bookmark(self):
        self.page.btn_popup_open.click()
        newBookmarkTitle = str(time.time())
        self.page.input_popup.send_keys(newBookmarkTitle)
        self.page.btn_create_bookmark.click()
        List = self.page.bookmark_title
        flag = False
        for i in List:
            if i.text == newBookmarkTitle:
                flag =  True
        self.assertEqual(flag, True)
