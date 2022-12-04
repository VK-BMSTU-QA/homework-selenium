from pageobjects.base import component
from selenium.webdriver.common.by import By


class Card(component.Component):
    @staticmethod
    def create(driver):
        card = Card(driver, "#root > div.taskBlockContainer.taskBlock_active > div.taskBlock")
        card.locate()
        return card