from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class CartPage(BaseComponent):
    locators = locators.CartLocators()
    PATH = paths.GUAVA_DISHES

    FIRST_DISH_NUM = 1

    def add_to_cart(self, number=FIRST_DISH_NUM):
        self.click(self.locators.ADD_TO_CART_BUTTON[number - 1])

    def get_count_of_dish(self, number=FIRST_DISH_NUM):
        return int(self.find(self.locators.COUNT_OF_DISH_IN_CART[number - 1]).text)

    def get_price_of_dish_in_cart(self, number=FIRST_DISH_NUM):
        return self.find(self.locators.PRICE_OF_DISH_IN_CART[number - 1]).text

    def get_price_of_dish_in_menu(self, number=FIRST_DISH_NUM):
        return self.find(self.locators.PRICE_OF_DISH_IN_MENU[number - 1]).text

    def decrement_dish_in_cart(self, number=FIRST_DISH_NUM):
        self.click(self.locators.DECREMENT_DISH_COUNT[number - 1])

    def increment_dish_in_cart(self, number=FIRST_DISH_NUM):
        self.click(self.locators.INCREMENT_DISH_COUNT[number - 1])

    def is_dish_visible(self, number=FIRST_DISH_NUM):
        return self.is_visible(self.locators.DISH_IN_CART[number - 1])
