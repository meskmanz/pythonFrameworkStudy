from selenium.webdriver.common.by import By

from components.top_menu_page import TopMenuComponent
from pages.accout_register_page import AccountRegisterPage


class LoginPage(AccountRegisterPage, TopMenuComponent):
    __existing_client_label_xpath = '//div[@class="well"]/h2'

    def existing_client_label(self):
        return self.driver.find_element(By.XPATH, self.__existing_client_label_xpath)