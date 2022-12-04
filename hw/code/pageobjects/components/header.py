from pageobjects.base import component
from selenium.webdriver.common.by import By


class Header(component.Component):
    @staticmethod
    def create(driver):
        header = Header(driver, "header.header")
        header.locate()
        return header
