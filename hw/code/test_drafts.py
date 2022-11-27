import pytest

from hw.code.pages.auth import AuthPage
from pages.send import SendPage
import random


def test_create_draft(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login("seleniumtest", "seleniumtest")

    send_page = SendPage(browser)
    send_page.go_to_site()
    send_page.create_draft("test address", "test theme", "test text")
