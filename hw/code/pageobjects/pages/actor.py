from selenium.webdriver.common.by import By

from pageobjects.base.page import Page
import os
import time

class ActorPage(Page):
    @property
    def actor_movies(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="movie__body__info__data__title__movie-title")

    def open(self):
        super().open('actors/90')



