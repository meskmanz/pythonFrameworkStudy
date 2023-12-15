from pages.accout_register_page import AccountRegisterPage
from pages.home_page import HomePage
from utils.random_values import random_string, random_number


class TestHomePage:

    def test_logo(self, browser):
        hp = HomePage(browser)
        assert hp.logo_img().is_displayed()

    def test_search(self, browser):
        text = 'Something'
        hp = HomePage(browser)
        hp.search(text)
        assert text in hp.result_label().text

    def test_register_user(self, browser):
        text = 'Ваш обліковий запис успішно створено!'
        hp = HomePage(browser)
        hp.open_registration_form()
        arp = AccountRegisterPage(browser)
        email = f'{random_string()}@gmail.com'
        arp.fill_the_form(firstname='Pavlo', lastname='V', email=email, phone=random_number(),
                          address='1 New Ave', city='Lviv', country='Ukraine', region="L'vivs'ka Oblast'",
                          password='test', confirm_password='test', agree=True, submit=True)
        assert hp.result_label().text == text
