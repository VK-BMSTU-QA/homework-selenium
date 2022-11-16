from pageobjects.base import component
from selenium.webdriver.common.by import By


class Header(component.Component):
    @staticmethod
    def create(driver):
        header = Header(driver, "header.header")
        header.locate()
        return header

    @property
    def span_user_name(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="header")

    @property
    def user_name(self):
        return self.span_user_name.text
