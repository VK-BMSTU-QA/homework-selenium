from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class MainPage(BaseComponent):
    locators = locators.MainPageLocators()
    PATH = paths.MAIN

    def choose_sushi_category(self):
        self.click(self.locators.SUSHI_CATEGORY_BUTTON)
        self.wait_visability_of_elem(self.locators.SUSHI_CATEGORY_SELECTED_BUTTON)

    def unchoose_sushi_category(self):
        self.click(self.locators.SUSHI_CATEGORY_BUTTON)
        self.wait_invisability_of_elem(self.locators.SUSHI_CATEGORY_SELECTED_BUTTON)


    def choose_pizza_category(self):
        self.click(self.locators.PIZZA_CATEGORY_BUTTON)
        self.wait_visability_of_elem(self.locators.PIZZA_CATEGORY_SELECTED_BUTTON)
