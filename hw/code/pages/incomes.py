from .base import BasePage

from .locators.income import IncomeLocators


class IncomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, add_url="income")

    def list_count(self) -> int:
        items = self.find_elements(IncomeLocators.INCOMES, soft=True)
        return len(items)
