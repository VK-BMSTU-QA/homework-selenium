from selenium.webdriver.common.by import By

visible = '[style="visibility: visible;"]'


class SendLocators:
    ADDRESS_INPUT = (By.ID, "inputLogin")
    THEME_INPUT = (By.ID, "themeInput")
    TEXT_INPUT = (By.ID, "textareaMain")
    SEND_BUTTON = (By.ID, "sendButton")
    MENU_DRAFT_BUTTON = (By.ID, "draft")

