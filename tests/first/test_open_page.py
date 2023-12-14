from pages.home_page.home_page import HomePage


class TestHomePage:

    def test_logo(self, browser):

        hp = HomePage(browser)
        assert hp.logo_img().is_displayed()

    def test_search(self, browser):
        hp = HomePage(browser)
        hp.search("Something")
        pass
