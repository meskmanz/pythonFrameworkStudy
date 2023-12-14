import string

from pages.accout_register_page import AccountRegisterPage
from pages.home_page import HomePage
from utils.string import random_string


class TestHomePage:

    def test_logo(self, browser):
        hp = HomePage(browser)
        assert hp.logo_img().is_displayed()

    def test_search(self, browser):
        hp = HomePage(browser)
        hp.search("Something")
        assert True

    def test_register_user(self, browser):
        hp = HomePage(browser)
        hp.open_registration_form()
        arp = AccountRegisterPage(browser)
        email = f'{random_string()}@gmail.com'
        arp.fill_the_form(firstname='Pavlo', lastname='V', email=email, phone=random_string(chars=string.digits),
                          address='1 New Ave', city='Lviv', country='Ukraine', region="L'vivs'ka Oblast'",
                          password='test', confirm_password='test', agree=True, submit=True)
        assert True
