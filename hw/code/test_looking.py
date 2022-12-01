import os

from pages.auth import AuthPage
from pages.outcomes import OutcomePage
from pages.sends import SendPage, SendInfo
from dotenv import load_dotenv

load_dotenv()  # LOGIN and PASSWORD

SAMPLE_MESSAGE = SendInfo(address=os.getenv('LOGIN'), theme='first test theme', text='1 test text')


def test_success_reply(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    send_page = SendPage(browser)
    send_page.go_to_site()
    send_page.create_message(SAMPLE_MESSAGE)

    outcoming_page = OutcomePage(browser)
    outcoming_page.go_to_site()
    outcoming_page.go_to_look(0)
    outcoming_page.reply()

    assert outcoming_page.is_redirected('send')
    assert outcoming_page.get_theme() == "Re(1): " + SAMPLE_MESSAGE.theme
    assert outcoming_page.get_address() == os.getenv('LOGIN')


def test_success_forward(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    send_page = SendPage(browser)
    send_page.go_to_site()
    send_page.create_message(SAMPLE_MESSAGE)

    outcoming_page = OutcomePage(browser)
    outcoming_page.go_to_site()
    outcoming_page.go_to_look(1)
    outcoming_page.forward()

    assert outcoming_page.is_redirected('send')
    assert outcoming_page.get_theme() == SAMPLE_MESSAGE.theme
    assert outcoming_page.get_address() == ''

def test_success_delete(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    send_page = SendPage(browser)
    send_page.go_to_site()
    send_page.create_message(SAMPLE_MESSAGE)

    outcoming_page = OutcomePage(browser)
    outcoming_page.go_to_site()
    prev = outcoming_page.list_count()
    outcoming_page.go_to_look(2)
    outcoming_page.delete()

    assert outcoming_page.is_redirected('income')
    outcoming_page.go_to_site()
    assert prev - 1 == outcoming_page.list_count()
