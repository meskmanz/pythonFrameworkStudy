import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service

from utils.logger import Logger


class Driver:
    def __init__(self, browser, headless=False):
        self._browser = self._driver(browser, headless)

    def _driver(self, browser, headless):
        Logger().log().info(f'Launch {browser} browser')
        if browser.lower() == 'chrome':
            web_driver = self._chrome_driver(headless=headless)
        elif browser.lower() == 'firefox':
            web_driver = self._firefox_driver(headless=headless)
        else:
            raise Exception(f'{browser} is not supported browsers')
        web_driver.implicitly_wait(10)  # seconds
        return web_driver

    def _chrome_driver(self, headless):
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-gpu')
        if headless:
            chrome_options.add_argument('--headless')
        if platform.system() == 'Linux':
            service = Service('/usr/lib/chromium-browser/chromedriver')
            return webdriver.Chrome(options=chrome_options, service=service)
        else:
            return webdriver.Chrome(options=chrome_options)

    def _firefox_driver(self, headless):
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        return webdriver.Firefox(options=firefox_options)

    def get_browser(self):
        return self._browser
