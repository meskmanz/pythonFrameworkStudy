from selenium.webdriver.common.by import By

from components.top_menu_component import TopMenuComponent
from pages.accout_register_page import AccountRegisterPage


class LoginPage(AccountRegisterPage):
    __existing_client_label_xpath = (By.XPATH, '//div[@class="well"]/h2')
    __alert_message_xpath = (By.XPATH, '//div[contains(@class, "alert")]')

    def __init__(self, driver):
        super().__init__(driver)
        self.top_menu = TopMenuComponent(driver)

    def existing_client_label(self):
        return self.find_element(self.__existing_client_label_xpath)

    def alert_message(self):
        return self.find_element(self.__alert_message_xpath)
