from pages.accout_register_page import AccountRegisterPage
from pages.home_page import HomePage


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
        arp.fill_the_form(firstname='Pavlo', lastname='V', email='test@mail.com', phone='123', address='1 New Ave',
                          city='Lviv', country='Ukraine', region="L'vivs'ka Oblast'")
        assert True
