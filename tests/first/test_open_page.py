import pytest

from pages.home_page import HomePage


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


