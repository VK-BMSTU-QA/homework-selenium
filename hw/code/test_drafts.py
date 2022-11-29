import os

from hw.code.pages.auth import AuthPage
from hw.code.pages.drafts import DraftPage
from hw.code.pages.drafts import Draft
from dotenv import load_dotenv

load_dotenv()
sample_draft = Draft('1 test address', '1 test theme', '1 test text')

def test_create_draft(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_count = draft_page.count()
    sample_draft = Draft('test address', 'test theme', 'test text')
    draft_page.create_draft(sample_draft)
    draft_page.go_to_site()
    draft_page.driver.refresh()
    assert draft_count == draft_page.count() + 1


def test_create_draft_cancel(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_count = draft_page.count()
    draft_page.create_draft('test address', 'test theme', 'test text', cancel=True)
    draft_page.go_to_site()
    assert draft_count == draft_page.count()


def test_show_draft_list(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.create_draft('1 test address', '1 test theme', '1 test text')
    draft_page.create_draft('2 test address', '2 test theme', '2 test text')

    draft_page.go_to_site()
    assert draft_count == len(draft_page.list())


def test_delete_draft(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_page.create_draft('1 test address', '1 test theme', '1 test text')
    assert draft_page.count() > 0
    draft_page.delete_all()
    assert draft_page.count() == 0


def test_show_draft(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_page.delete_all()
    draft_page.create_draft(sample_draft)
    opened_draft = draft_page.open_draft(index=0)
    assert opened_draft.address == sample_draft.address
    assert opened_draft.theme == sample_draft.theme
    assert opened_draft.text == sample_draft.text
