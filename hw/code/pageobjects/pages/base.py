from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class BasePage(Page):

    def open(self, *args, **kwargs):
        super().open("")
    
