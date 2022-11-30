from ui.locators import locators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class ReviewsElement(BaseComponent):
    locators = locators.ReviewsLocators()
    PATH = paths.MAIN
    SEND_REVIEW_PATH = paths.MAIN

    def go_to_review(self):
        self.click(self.locators.REVIEW_INFO_BLOCK)
        self.wait_visability_of_elem(self.locators.REVIEWS_HEADER)

    def input_review(self, text, stars):
        self.send_keys(self.locators.REVIEW_TEXTAREA, text)
        self.click(self.locators.REVIEW_STARS_BUTTONS[stars - 1])

    def send_review(self):
        self.click(self.locators.SEND_REVIEW_CONTENT_BUTTON)
        self.wait_visability_of_elem(self.locators.REVIEWS_HEADER)

    def get_first_review_text(self):
        return self.get_elem_text(self.locators.REVIEW_TEXT)[1]

    def get_first_review_stars(self):
        return self.get_elem_text(self.locators.REVIEW_STARS)[1]
