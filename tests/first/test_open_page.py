import pytest

from pages.accout_register_page import AccountRegisterPage
from pages.home_page import HomePage
from utils.random_values import random_string, random_number


class TestHomePage:

    def test_logo(self, setup):
        hp = HomePage(setup)
        assert hp.logo_img().is_displayed()

    @pytest.mark.parametrize("text", [
        ('Something'),
        ('New search'),
        ('Other things')
    ])
    def test_search(self, setup, text):
        hp = HomePage(setup)
        hp.search(text)
        assert text in hp.result_label().text

    def test_search2(self, setup, test_data):
        hp = HomePage(setup)
        hp.search(test_data)
        assert test_data in hp.result_label().text

    @pytest.mark.skip
    def test_register_user(self, setup):
        text = 'Ваш обліковий запис успішно створено!'
        hp = HomePage(setup)
        hp.open_registration_form()
        arp = AccountRegisterPage(setup)
        email = f'{random_string()}@gmail.com'
        arp.fill_the_form(firstname='Pavlo', lastname='V', email=email, phone=random_number(),
                          address='1 New Ave', city='Lviv', country='Ukraine', region="L'vivs'ka Oblast'",
                          password='test', confirm_password='test', agree=True, submit=True)
        assert hp.result_label().text == text
