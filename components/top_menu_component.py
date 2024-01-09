from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class TopMenuComponent(BaseComponent):
    __account_xpath = '//div[@id="top-links"]/ul/li/a[@class="dropdown-toggle"]'
    __register_xpath = '//div[@id="top-links"]//a[contains(@href, "register")]'
    __login_xpath = '//div[@id="top-links"]//a[contains(@href, "login")]'
    __logout_xpath = '//div[@id="top-links"]//a[contains(@href, "logout")]'

    def account_btn(self):
        return self.driver.find_element(By.XPATH, self.__account_xpath)

    def register_btn(self):
        return self.driver.find_element(By.XPATH, self.__register_xpath)

    def login_btn(self):
        return self.driver.find_element(By.XPATH, self.__login_xpath)

    def logout_btn(self):
        return self.driver.find_element(By.XPATH, self.__logout_xpath)

    def open_registration_form(self):
        self.log.info('Open registration form')
        self.account_btn().click()
        self.register_btn().click()

    def open_login_form(self):
        self.log.info('Open login form')
        self.account_btn().click()
        self.login_btn().click()
