import os

from pages.auth import AuthPage
from pages.outcomes import OutcomePage
from pages.sends import SendPage, SendInfo
from dotenv import load_dotenv

load_dotenv()  # LOGIN and PASSWORD



longs = [SendInfo('1 test address', '1 test long long long long long long long long long theme',
                               '1 test text'),
SendInfo('1 test long long long long long long long long long address', '1 test theme',
                                 '1 test text')]

wrong_address = [SendInfo('', 'sda', ''), SendInfo('wrong_name', 'asd', '')]

SAMPLE_EMPTY_MESSAGE = SendInfo(address='', theme='', text='1 test text')
SAMPLE_MESSAGE = SendInfo(address='', theme='1 test theme', text='1 test text')


def test_wrong_adress_of_receiptor(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    for wa in wrong_address:
        send_page = SendPage(browser)
        send_page.go_to_site()
        send_page.create_message(wa)
        assert send_page.is_wrong()


def test_create_message_empty(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    outcoming_page = OutcomePage(browser)
    outcoming_page.go_to_site()
    prev = outcoming_page.list_count()

    for l in longs:
        send_page = SendPage(browser)
        send_page.go_to_site()
        send_page.create_message(l)

    outcoming_page.go_to_site()
    after = outcoming_page.list_count()

    assert prev == after


def test_empty_them(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    send_page = SendPage(browser)
    send_page.go_to_site()
    SAMPLE_EMPTY_MESSAGE.address = os.getenv('LOGIN')
    send_page.create_message(SAMPLE_EMPTY_MESSAGE)
    assert send_page.is_dialog_appear()


def test_success_send(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    outcoming_page = OutcomePage(browser)
    outcoming_page.go_to_site()
    prev = outcoming_page.list_count()

    send_page = SendPage(browser)
    send_page.go_to_site()
    SAMPLE_MESSAGE.address = os.getenv('LOGIN')
    send_page.create_message(SAMPLE_MESSAGE)

    outcoming_page.go_to_site()
    after = outcoming_page.list_count()

    assert prev + 1 == after
