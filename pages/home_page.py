import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class HomePage(BasePage):
    _logo_xpath = '//div[@id="logo"]/a/img'
    _search_form_xpath = '//div[@id="search"]'
    _search_textfield_xpath = f'{_search_form_xpath}/input'
    _search_btn_xpath = f'{_search_form_xpath}/span/button'
    _account_xpath = '//div[@id="top-links"]/ul/li/a[@class="dropdown-toggle"]'
    _register_xpath = '//div[@id="top-links"]//a[contains(@href, "register")]'
    _result_label_xpath = '//div[@id="content"]/h1'

    # Elements

    def logo_img(self):
        return self.driver.find_element(By.XPATH, self._logo_xpath)

    def search_text_field(self):
        return self.driver.find_element(By.XPATH, self._search_textfield_xpath)

    def search_btn(self):
        return self.driver.find_element(By.XPATH, self._search_btn_xpath)

    def account_btn(self):
        return self.driver.find_element(By.XPATH, self._account_xpath)

    def register_btn(self):
        return self.driver.find_element(By.XPATH, self._register_xpath)

    def result_label(self):
        return self.driver.find_element(By.XPATH, self._result_label_xpath)

    # Business Logic

    def search(self, text):
        logging.info(f'Do search for: {text}')
        self.search_text_field().send_keys(text)
        self.search_btn().click()

    def open_registration_form(self):
        logging.info('Open registration form')
        self.account_btn().click()
        self.register_btn().click()
