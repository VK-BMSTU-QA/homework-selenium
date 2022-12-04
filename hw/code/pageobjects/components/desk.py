from pageobjects.base import component
from selenium.webdriver.common.by import By


class Desk(component.Component):
    @staticmethod
    def create(driver):
        desk = Desk(driver, "#root > div.main__content > a")
        desk.locate()
        return desk