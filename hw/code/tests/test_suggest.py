import pytest
from ui.paths import paths
from ui.components.suggests_page import SuggestPage
from ui.base_case.base_case import BaseCase


class TestSuggestPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = SuggestPage(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, set_page):
        self.page.open_path(paths.MAIN)

    MOSCOW_SUGGEST = "Москва,"
    FULL_ADDRESS = "Москва, Кравченко Улица, 22"
    EXTRA_LIDER_SPACE_MOSCOW = " Москва"
    LOWCASE_MOSCOW = "москва"

    def test_saved_address(self, set_address, open):
        old_address_input, old_address_value = self.page.get_address_value()
        assert self.page.is_active(old_address_input)
        self.page.close_address_input()

        assert self.page.is_url_matches(paths.MAIN)
        new_address_input, new_address_value = self.page.get_address_value()
        assert not self.page.is_active(new_address_input)
        assert self.page.is_invisible(self.page.locators.SUGGESTS)
        assert new_address_value == old_address_value

    @pytest.mark.parametrize(
        "query,expected_suggest",
        [
            (MOSCOW_SUGGEST, MOSCOW_SUGGEST),
            (EXTRA_LIDER_SPACE_MOSCOW, MOSCOW_SUGGEST),
            (LOWCASE_MOSCOW, MOSCOW_SUGGEST),
        ],
    )
    def test_suggest(self, open, query, expected_suggest):
        self.page.get_suggests(query)
        assert self.page.get_text_first_suggest() == expected_suggest

    def test_choose_suggest(self, open):
        self.page.get_suggests("М")
        assert self.page.get_text_first_suggest() == self.MOSCOW_SUGGEST
        self.page.choose_first_suggest()

        new_address_input, new_address_value = self.page.get_address_value()
        assert self.page.is_active(new_address_input)
        assert self.page.get_value(new_address_input) == self.MOSCOW_SUGGEST

    def test_full_address(self, open):
        self.page.get_suggests_full_address(self.FULL_ADDRESS)
        assert self.page.get_text_first_suggest() == self.FULL_ADDRESS
        self.page.choose_first_suggest()

        new_address_input, new_address_value = self.page.get_address_value()
        assert self.page.is_invisible(self.page.locators.SUGGESTS)
        assert not self.page.is_active(new_address_input)
        assert new_address_value == self.FULL_ADDRESS
        assert self.page.is_url_matches(paths.MAIN)

    def test_full_address_suggests(self, open):
        self.page.get_suggests(self.MOSCOW_SUGGEST)
        self.page.choose_first_suggest()
        self.page.choose_first_suggest()
        first_suggest_text = self.page.get_text_first_suggest()
        self.page.choose_first_suggest()

        new_address_input, new_address_value = self.page.get_address_value()
        assert new_address_value == first_suggest_text
        assert self.page.is_invisible(self.page.locators.SUGGESTS)
        assert not self.page.is_active(new_address_input)
        assert self.page.is_url_matches(paths.MAIN)
