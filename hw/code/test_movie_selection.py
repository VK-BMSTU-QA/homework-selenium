import os.path
import time

from selenium.webdriver import ActionChains

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.base_case import BaseCase


class TestArrowsClick(BaseCase):
    authorize = True
    button_right = BasePage.locators.BUTTON_ARROW_RIGHT
    button_left = BasePage.locators.BUTTON_ARROW_LEFT

    

    def test_arrows_clicking(self):
        time.sleep(3)
        selection = self.base_page.wait_visability_of_elem(BasePage.locators.SELECTION)
         selection = (self.base_page.driver.find_elements_by_xpath(BasePage.locators.SELECTION[1])[0])
        ActionChains(self.driver).move_to_element(selection).perform()
        child_selection = self.base_page.wait_visability_of_elem(BasePage.locators.CHILD_SELECTION)
         child_selection = (self.base_page.driver.find_elements_by_xpath(BasePage.locators.CHILD_SELECTION[1])[0])
        for k in [self.button_right, self.button_left]:
            before_style = child_selection.value_of_css_property('transform')
            self.base_page.click(k, 10)
            time.sleep(3)
            assert child_selection.value_of_css_property('transform') != before_style


class TestArrowsShow(BaseCase):
    authorize = True
    button_right = BasePage.locators.BUTTON_ARROW_RIGHT
    button_left = BasePage.locators.BUTTON_ARROW_LEFT

    def test_arrows_show(self):
        time.sleep(3)
        selection = self.base_page.wait_visability_of_elem(BasePage.locators.SELECTION)
         selection = (self.base_page.driver.find_elements_by_xpath(BasePage.locators.SELECTION[1])[0])
        self.base_page.click(self.button_right, 10)

        ActionChains(self.driver).move_to_element(selection).perform()
        for button in [self.button_right, self.button_left]:
            time.sleep(1)
            button = (self.base_page.driver.find_elements_by_xpath(button[1])[0])
            assert 'hover' in button.get_attribute("class")
            time.sleep(2)


class TestArrowsHidden(BaseCase):
    authorize = True
    button_right = BasePage.locators.BUTTON_ARROW_RIGHT
    button_left = BasePage.locators.BUTTON_ARROW_LEFT

    def test_arrows_unshow(self):
        time.sleep(3)
        selection = self.base_page.wait_visability_of_elem(BasePage.locators.SELECTION)
        selection = (self.base_page.driver.find_elements_by_xpath(BasePage.locators.SELECTION[1])[0])
        ActionChains(self.driver).move_to_element(selection).perform()
        button_left = (self.base_page.driver.find_elements_by_xpath(self.button_left[1])[0])
        button_right = (self.base_page.driver.find_elements_by_xpath(self.button_right[1])[0])
        assert button_left.value_of_css_property('visibility') == 'hidden'
        assert button_right.value_of_css_property('visibility') == 'visible'
        self.base_page.click(self.button_right, 10)
        self.base_page.click(self.button_right, 10)
        self.base_page.click(self.button_right, 10)
        time.sleep(3)
        assert button_right.value_of_css_property('visibility') == 'hidden'
        assert button_left.value_of_css_property('visibility') == 'visible'
