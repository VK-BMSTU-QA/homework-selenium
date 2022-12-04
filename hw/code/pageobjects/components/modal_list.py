from pageobjects.base import component
from selenium.webdriver.common.by import By


class ModalList(component.Component):
    @staticmethod
    def create(driver):
        modal = ModalList(driver, "#modalBlock > div > div")
        modal.locate()
        return modal
