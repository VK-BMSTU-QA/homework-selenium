from selenium.webdriver.common.by import By


class BasePageLocators:
    HTML = (By.TAG_NAME, "html")
    CART_BUTTON = (By.ID, "shoppingCartButton")
    CART = (By.CLASS_NAME, "shopping-cart")
    GUAVA_RESTAURANT_IMG = (By.XPATH, '//img[@class="rest-icon__rest_img" and @alt="Guava"]')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "dish-icon__button-add-to-order")
    # PROFILE_MENU = (By.CLASS_NAME, "profile-preview__menu")
    # LOGIN_MODAL = (By.ID, "modal")
    # SUGGESTS = (By.CLASS_NAME, "suggest-form__suggest-row")
    # ADDRESS_INPUT = (By.ID, "suggestsSearch")
    LOGO_BUTTON = (By.XPATH, '//a[@class="main-button__controller" and text() = "obringTo"]')


class HeaderLocators(BasePageLocators):
    LOGIN_MODAL = (By.ID, "modal")
    PROFILE_BUTTON = (By.ID, "profilePreviewButton")
    GUAVA_RESTAURANT_IMG = (By.XPATH, '//img[@class="rest-icon__rest_img" and @alt="Guava"]')
    PROFILE_MENU = (By.CLASS_NAME, "profile-preview__menu")
    ADDRESS_INPUT = (By.ID, "suggestsSearch")
    SUGGESTS = (By.CLASS_NAME, "suggest-form__suggest-row")
    LOGO_BUTTON = (By.XPATH, '//a[@class="main-button__controller" and text() = "obringTo"]')
    LOGIN_BUTTON = (By.XPATH, '//nav[@data-section="login"]')
    SEARCH_BUTTON = (By.ID, "searchButton")
    SEARCH_CLOSE_BUTTON = (By.ID, "closeSearchImg")
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_AREA = (By.ID, "searchActivatedAria")
    CART_BUTTON = (By.ID, "shoppingCartButton")
    CART = (By.CLASS_NAME, "shopping-cart")


class MainPageLocators(BasePageLocators):
    MENU_HEADER = (By.XPATH, '//h1[@class="simple-title"]')
    PROMOCODE_IMG = (By.CLASS_NAME, "promo-code-block__promo-code-icon")
    PROMOCODE_UI_NOTIFICATION = (By.XPATH, '//div[@class="notification__message" and text() = "Промокод успешно применен"]')
    SUSHI_CATEGORY_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and @data-title = "Суши"]')
    SUSHI_CATEGORY_SELECTED_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and contains(@class, "category_selected") and @data-title = "Суши"]')
    PIZZA_CATEGORY_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and @data-title = "Пицца"]')
    PIZZA_CATEGORY_SELECTED_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and contains(@class, "category_selected") and @data-title = "Пицца"]')


class LoginLocators(BasePageLocators):
    PROFILE_BUTTON = (By.ID, "profilePreviewButton")
    LOGIN_MODAL = (By.ID, "modal")
    PHONE_INPUT = (By.XPATH, '//div[@id="loginPhone"]//input[@class="input-block__input"]')
    LOGIN_BUTTON = (By.ID, "loginButton")
    CODE_INPUT = (By.XPATH, '//div[@id="confirmCode"]//input[@class="input-block__input"]')
    CONFIRM_CODE_BUTTON = (By.ID, "confirmCodeButton")
