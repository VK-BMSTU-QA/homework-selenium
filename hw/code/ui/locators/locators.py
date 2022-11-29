from selenium.webdriver.common.by import By


class BasePageLocators:
    HTML = (By.TAG_NAME, "html")
    CART_BUTTON = (By.ID, "shoppingCartButton")
    CART = (By.CLASS_NAME, "shopping-cart")
    GUAVA_RESTAURANT_IMG = (By.XPATH, '//img[@class="rest-icon__rest_img" and @alt="Guava"]')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "dish-icon__button-add-to-order")
    ORDER_BUTTON = (By.ID, "orderButton")
    PAY_BUTTON = (By.ID, "buttonPay")
    LOGO_BUTTON = (By.XPATH, '//a[@class="main-button__controller" and text() = "obringTo"]')
    ORDER_HISTORY_HEADER = (By.XPATH, '//h1[@class="form-title__title-name" and text() = "Мои заказы"]')


class HeaderLocators(BasePageLocators):
    LOGIN_MODAL = (By.ID, "modal")
    PROFILE_BUTTON = (By.ID, "profilePreviewButton")
    GUAVA_RESTAURANT_IMG = (By.XPATH, '//img[@class="rest-icon__rest_img" and @alt="Guava"]')
    PROFILE_MENU = (By.CLASS_NAME, "profile-preview__menu")
    ADDRESS_INPUT = (By.ID, "suggestsSearch")
    SUGGESTS = (By.CLASS_NAME, "suggest-form__suggest-row")
    LAST_SUGGEST = (By.XPATH, '//div[@class="suggest-form__suggest-row"][last()]')
    LOGO_BUTTON = (By.XPATH, '//a[@class="main-button__controller" and text() = "obringTo"]')
    LOGIN_BUTTON = (By.XPATH, '//nav[@data-section="login"]')
    SEARCH_BUTTON = (By.ID, "searchButton")
    SEARCH_CLOSE_BUTTON = (By.ID, "closeSearchImg")
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_AREA = (By.ID, "searchActivatedAria")
    CART_BUTTON = (By.ID, "shoppingCartButton")
    CART = (By.CLASS_NAME, "shopping-cart")
    RESTAURANTS_HEADER = (By.XPATH, '//a[@class="links-block__main-link" and text() = "Рестораны"]')


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


class OrderHistoryLocators(BasePageLocators):
    DETAILS_BUTTON = (By.CLASS_NAME, "buttonOpenClose")
    ORDER_DETAILS = (By.CLASS_NAME, "order__main-content")
    GO_TO_ALL_RESTAURANTS = (By.CLASS_NAME, "back-button__img")
    RESTAURANTS_HEADER = (By.XPATH, '//a[@class="links-block__main-link" and text() = "Рестораны"]')


class SearchPageLocators(BasePageLocators):
    SEARCH_BUTTON = (By.ID, "searchButton")
    SEARCH_CLOSE_BUTTON = (By.ID, "closeSearchImg")
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_AREA = (By.ID, "searchActivatedAria")
    RESTAURANT_CART = (By.CLASS_NAME, "restaurants-form__rest_icon")
    RESTAURANT_CART_NAME = (By.CLASS_NAME, "rest-icon__rest-name")
    NOTHING_FOUND_MESSAGE = (By.XPATH, '//div[@class="restaurants-form__empty-rest-list" and contains(text()," ничего не найдено. Попробуйте ввести другой ресторан или категорию")]')
    TOO_LONG_UI_NOTIFICATION = (By.XPATH, '//div[@class="notification__message" and text() = "Извините, но название ресторана не может превышать 100 символов."]')
    UI_NOTIFICATION = (By.XPATH, '//div[@class="notification__message"]')
