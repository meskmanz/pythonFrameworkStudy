from selenium import webdriver


class Driver:
    browsers = {'chrome': webdriver.Chrome,
                'firefox': webdriver.Firefox}

    def __init__(self, browser='Chrome'):
        self._browser = self.get_browser(browser)

    def get_browser(self, browser):
        return self.browsers[browser.lower()]()

    @property
    def browser(self):
        return self._browser
