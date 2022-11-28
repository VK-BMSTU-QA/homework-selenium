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
    PROMOCODE_UI_NOTIFICATION = (
        By.XPATH, '//div[@class="notification__message" and text() = "Промокод успешно применен"]')
    SUSHI_CATEGORY_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and @data-title = "Суши"]')
    SUSHI_CATEGORY_SELECTED_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "category ") and contains(@class, "category_selected") and @data-title = "Суши"]')
    PIZZA_CATEGORY_BUTTON = (By.XPATH, '//div[contains(@class, "category ") and @data-title = "Пицца"]')
    PIZZA_CATEGORY_SELECTED_BUTTON = (By.XPATH,
                                      '//div[contains(@class, "category ") and contains(@class, "category_selected") and @data-title = "Пицца"]')


class LoginLocators(BasePageLocators):
    PROFILE_BUTTON = (By.ID, "profilePreviewButton")
    LOGIN_MODAL = (By.ID, "modal")
    PHONE_INPUT = (By.XPATH, '//div[@id="loginPhone"]//input[@class="input-block__input"]')
    LOGIN_BUTTON = (By.ID, "loginButton")
    CODE_INPUT = (By.XPATH, '//div[@id="confirmCode"]//input[@class="input-block__input"]')
    CONFIRM_CODE_BUTTON = (By.ID, "confirmCodeButton")


class RestaurantMenuLocators(BasePageLocators):
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "dish-icon__button-add-to-order")
    CART = (By.CLASS_NAME, "shopping-cart")
    FOBRINGTO_BUTTON = (By.CLASS_NAME, "page-header__button")
    RESTAURANTS_LIST = (By.CLASS_NAME, "restaurants-form")


class CardLocators(BasePageLocators):
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'dish-icon__button-add-to-order')
    CART = (By.CLASS_NAME, "shopping-cart")
    DECREMENT_DISH_COUNT = (By.CLASS_NAME, "decrementDishCount")
    INCREMENT_DISH_COUNT = (By.CLASS_NAME, 'incrementDishCount')
    COUNT_OF_DISHES = (By.CLASS_NAME, "point-info__count-current-point")
    PRICE = (By.CLASS_NAME, "button__controller_with-price")
    ADD_SECOND_DISH = (By.XPATH, '//*[@id="root"]/main/div[3]/section[2]/div[2]/div[4]/button')
    SECOND_DISH_IN_CARD = (By.XPATH, '//*[@id="modal"]/div/div[2]/section[2]/div[2]/div[1]/div[1]')
    COUNT_SECOND_DISHES = (By.XPATH, '//*[@id="modal"]/div/div[2]/section[2]/div[2]/div[3]/div[2]')
    ORDER_BUTTON = (By.ID, "orderButton")


class RecommendationsLocators(BasePageLocators):
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'dish-icon__button-add-to-order')
    RECOMMENDATIONS = (By.CLASS_NAME, 'shopping-cart__recommendations')
    ADD_RECOMMENDATIONS = (By.CLASS_NAME, 'recommendation__button-add-to-order')
    RECOMMENDATION_DISH_IN_CARD = (By.XPATH, '//*[@id="modal"]/div/div[2]/section[2]')


class PromoCodesLocators(BasePageLocators):
    PROMO_CODE = (By.CLASS_NAME, 'promo-code-block__promo-code-icon')
    PROMO_CODE_RESET = (By.CLASS_NAME, 'shopping-cart__preview-rest')


class CommentsLocators(BasePageLocators):
    RESTAURANTS = (By.CLASS_NAME, 'rest-icon__rest_img')
    COMMENTS_BLOCK = (By.CLASS_NAME, 'comments-block__value')
    ORDER_BUTTON = (By.ID, "orderButton")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'dish-icon__button-add-to-order')
