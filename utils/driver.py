from selenium import webdriver
from utils.logger import Logger


class Driver:
    web_drivers = {
        'chrome': webdriver.Chrome,
        'firefox': webdriver.Firefox
    }

    def __init__(self, browser):
        self._browser = self._driver(browser)

    def _driver(self, browser):
        if browser.lower() not in self.web_drivers.keys():
            raise Exception(f'{browser} is not supported browsers (supported browsers: {self.web_drivers.keys()})')
        Logger().log().info(f'Launch {browser} browser')
        web_driver = self.web_drivers[browser]()
        web_driver.implicitly_wait(10)  # seconds
        return web_driver

    def get_browser(self):
        return self._browser
