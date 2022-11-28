from pageobjects.pages.actor import ActorPage
from tests.base_test_case import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math
import os

MAX_REVIEW_LENGTH = 300

class ActorTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = ActorPage(self.driver)

    def test_actor_movies_present(self):
        self.page.open()
        self.assertGreater(len(self.page.actor_movies), 0)

    def test_actor_to_his_movie(self):
        self.page.open()
        self.page.actor_movies[0].click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("movies"))

