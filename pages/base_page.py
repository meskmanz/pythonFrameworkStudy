from selenium.webdriver.remote.webelement import WebElement

from utils.logger import Logger
from enum import Enum
from typing import Tuple
from selenium.common import ElementNotVisibleException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

Locator = Tuple[By, str]


class WaitType(Enum):
    DEFAULT = 20
    SHORT = 5
    LONG = 60
    FLUENT = 10


class BasePage(object):
    def __init__(self, driver):
        self.log = Logger().log()
        self.driver = driver
        self._wait = WebDriverWait(driver, WaitType.DEFAULT.value)
        self._short_wait = WebDriverWait(driver, WaitType.SHORT.value)
        self._long_wait = WebDriverWait(driver, WaitType.LONG.value)
        self._fluent_wait = WebDriverWait(driver, WaitType.FLUENT.value, poll_frequency=1,
                                          ignored_exceptions=[ElementNotVisibleException])

    def wait(self, locator: Locator, waiter: WebDriverWait = None) -> WebElement:
        if waiter is None:
            waiter = self._wait
        try:
            return waiter.until(ec.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not found after {waiter.timeout} seconds")

    def find_element(self, locator: Locator) -> WebElement:
        return self.wait(locator)

    def get_title(self):
        return self.driver.title
