from selenium.webdriver.common.by import By

from pageobjects.base.page import Page
import os
import time

class PremierePage(Page):
    @property
    def trailer_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="trailer__btn")

    @property
    def first_actor(self):
        return self.driver.find_element(by=By.XPATH, value='//a[@href="/actors/6368"]')

    @property
    def first_genre(self):
        return self.driver.find_element(by=By.XPATH, value='//a[@href="/genres/action"]')

    @property
    def first_alike_premiere(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="slider__list__track__item__link")

    @property
    def first_profile(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="review-card__info__title__name")

    def open(self):
        super().open('announced/8')



