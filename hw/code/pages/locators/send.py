from selenium.webdriver.common.by import By

visible = '[style="visibility: visible;"]'


class SendLocators:
    ADDRESS_INPUT = (By.ID, "inputLogin")
    THEME_INPUT = (By.ID, "themeInput")
    TEXT_INPUT = (By.ID, "textareaMain")
    FILE_INPUT = (By.ID, "inputTmp")
    SEND_BUTTON = (By.ID, "sendButton")
    MENU_DRAFT_BUTTON = (By.ID, "draft")
    MENU_INCOME_BUTTON = (By.ID, "income")
    POPUP_DRAFT_SAVE_BUTTON = (By.ID, 'create')
    POPUP_DRAFT_CANCEL_BUTTON = (By.ID, 'prev')
    EMPTY_THEM_BUTTON = (By.ID, 'primBtn')
    ERROR_BOX = (By.CLASS_NAME, 'messageErrorBoxL ')
