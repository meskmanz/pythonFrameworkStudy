from pages.base_page import BasePage
from utils.logger import Logger


class BaseComponent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.log = Logger().log()
        self.driver = driver
