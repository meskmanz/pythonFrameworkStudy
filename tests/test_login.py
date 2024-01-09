import pytest

from data.default_data import CredentialsStrings
from pages.home_page import HomePage
from pages.accout_register_page import AccountRegisterPage
from pages.login_page import LoginPage
from utils.random_values import random_number


class TestLogin:

    @pytest.mark.skip
    def test_register_user(self, setup):
        text = 'Ваш обліковий запис успішно створено!'
        hp = HomePage(setup)
        hp.open_registration_form()
        arp = AccountRegisterPage(setup)
        password = CredentialsStrings().random_password
        arp.fill_the_form(firstname='Pavlo', lastname='V', email=CredentialsStrings().random_email,
                          phone=random_number(), address='1 New Ave', city='Lviv', country='Ukraine',
                          region="L'vivs'ka Oblast'", password=password, confirm_password=password, agree=True,
                          submit=True)
        assert hp.result_label().text == text

    def test_login_valid_creds(self, setup):
        hp = HomePage(setup)
        hp.open_login_form()
        lp = LoginPage(setup)
        lp.fill_the_form(email=CredentialsStrings().valid_email, password=CredentialsStrings().valid_password,
                         submit=True)
        lp.account_btn().click()
        assert lp.logout_btn().is_displayed()
