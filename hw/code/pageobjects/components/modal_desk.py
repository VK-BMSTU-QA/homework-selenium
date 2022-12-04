from pageobjects.base import component
from selenium.webdriver.common.by import By


class ModalDesk(component.Component):
    @staticmethod
    def create(driver):
        modal = ModalDesk(driver, "body > div.createDesk__bg.active > div")
        modal.locate()
        return modal