from selenium.webdriver.common.by import By

visible = '[style="visibility: visible;"]'


class HeaderLocators:
    HEADER = (By.CLASS_NAME, "parentHead")
    LOGO_BUTTON = (By.CLASS_NAME, "linked")
    COLOR_MENU_BUTTON = (By.ID, "color")
    BLUE_BUTTON = (By.ID, "blue")
    GREEN_BUTTON = (By.ID, "green")
    ORANGE_BUTTON = (By.ID, "orange")
    PINK_BUTTON = (By.ID, "pink")
    MENU_BUTTON = (By.CLASS_NAME, "profile")
    PROFILE_BUTTON = (By.ID, "profile")
    EXIT_BUTTON = (By.ID, "exit")

class MenuLocators:
    INCOME_BUTTON = (By.ID, "income")
    OUTCOME_BUTTON = (By.ID, "outcome")
    SEND_BUTTON = (By.ID, "send")
    DRAFT_BUTTON = (By.ID, "draft")
    SPAM_BUTTON = (By.ID, "spam")
