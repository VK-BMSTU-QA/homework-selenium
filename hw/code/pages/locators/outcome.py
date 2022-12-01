from selenium.webdriver.common.by import By

visible = '[style="visibility: visible;"]'


class OutcomeLocators:
    OUTCOMES = (By.CLASS_NAME, "messageText")
    SETTINGS = (By.ID, "settings")
    REMOVE = (By.ID, "remove")
    REMAIL = (By.ID, "reMail")
    FORWARD = (By.ID, "forward")

