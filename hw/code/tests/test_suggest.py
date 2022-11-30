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

    moscow_suggest = "Москва,"
    full_address = "Москва, Кравченко Улица, 22"

    def test_saved_address(self, set_address, open):
        old_address_input, old_address_value = self.page.get_address_value()
        assert self.page.is_active(old_address_input)
        self.page.close_address_input()

        assert self.page.is_url(paths.MAIN)
        new_address_input, new_address_value = self.page.get_address_value()
        assert not self.page.is_active(new_address_input)
        assert self.page.is_invisible(self.page.locators.SUGGESTS)
        assert new_address_value == old_address_value

    @pytest.mark.parametrize(
        "query,expected_suggest",
        [
            (moscow_suggest, moscow_suggest),
            (" Москва", moscow_suggest),
            ("москва", moscow_suggest),
        ],
    )
    def test_suggest(self, open, query, expected_suggest):
        self.page.get_suggests(query)
        assert self.page.is_first_suggest(expected_suggest)

    def test_choose_suggest(self, open):
        self.page.get_suggests("М")
        assert self.page.is_first_suggest(self.moscow_suggest)
        self.page.choose_first_suggest()

        new_address_input, new_address_value = self.page.get_address_value()
        assert self.page.is_active(new_address_input)
        assert self.page.has_value(new_address_input, self.moscow_suggest)

    def test_full_address(self,open):
        self.page.get_suggests_full_address(self.full_address)
        assert self.page.is_first_suggest(self.full_address)
        self.page.choose_first_suggest()

        new_address_input, new_address_value = self.page.get_address_value()
        assert self.page.is_invisible(self.page.locators.SUGGESTS)
        assert not self.page.is_active(new_address_input)
        assert new_address_value ==  self.full_address
        assert self.page.is_url(paths.MAIN)

    def test_full_address_suggests(self, open):
        self.page.get_suggests(self.moscow_suggest)
        self.page.choose_first_suggest()
        self.page.choose_first_suggest()
        first_suggest_text = self.page.get_elem_text_first_suggest()
        self.page.choose_first_suggest()

        new_address_input, new_address_value = self.page.get_address_value()
        assert new_address_value == first_suggest_text
        assert self.page.is_invisible(self.page.locators.SUGGESTS)
        assert not self.page.is_active(new_address_input)
        assert self.page.is_url(paths.MAIN)
