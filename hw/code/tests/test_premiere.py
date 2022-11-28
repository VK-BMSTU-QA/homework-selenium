from pageobjects.pages.premiere import PremierePage
from tests.base_test_case import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math
import os

MAX_REVIEW_LENGTH = 300

class PremiereTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = PremierePage(self.driver)

    def test_premiere_trailer(self):
        self.page.open()
        self.page.trailer_btn.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("youtube"))

    def test_premiere_to_actor(self):
        self.page.open()
        wait = WebDriverWait(self.driver, 10)
        self.page.first_actor.click()
        wait.until(EC.url_contains("actors"))

    def test_premiere_to_genre(self):
        self.page.open()
        wait = WebDriverWait(self.driver, 10)
        self.page.first_genre.click()
        wait.until(EC.url_contains("genres"))

    def test_premiere_to_alike_premiere(self):
        self.page.open()
        wait = WebDriverWait(self.driver, 10)
        self.page.first_alike_premiere.click()
        wait.until(EC.url_contains("announced"))
