from utils.logger import Logger


class BaseComponent(object):
    def __init__(self, driver):
        self.driver = driver
        self.log = Logger().log()
