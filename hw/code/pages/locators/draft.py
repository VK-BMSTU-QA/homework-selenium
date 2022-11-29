from selenium.webdriver.common.by import By

visible = '[style="visibility: visible;"]'


class DraftLocators:
    DRAFTS = (By.CLASS_NAME, "messageText")
    DELETE_BUTTON = (By.ID, "remove")
