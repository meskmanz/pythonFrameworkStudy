from selenium.webdriver.common.by import By

from components.top_menu_component import TopMenuComponent
from pages.base_page import BasePage
from utils.logger import Logger


class HomePage(BasePage, TopMenuComponent):
    __logo_xpath = '//div[@id="logo"]/a/img'
    __search_form_xpath = '//div[@id="search"]'
    __search_textfield_xpath = f'{__search_form_xpath}/input'
    __search_btn_xpath = f'{__search_form_xpath}/span/button'
    __result_label_xpath = '//div[@id="content"]/h1'
    log = Logger().log()

    # Elements

    def logo_img(self):
        return self.driver.find_element(By.XPATH, self.__logo_xpath)

    def search_text_field(self):
        return self.driver.find_element(By.XPATH, self.__search_textfield_xpath)

    def search_btn(self):
        return self.driver.find_element(By.XPATH, self.__search_btn_xpath)

    def result_label(self):
        return self.driver.find_element(By.XPATH, self.__result_label_xpath)

    # Business Logic

    def search(self, text):
        self.log.info(f'Do search for: {text}')
        self.search_text_field().send_keys(text)
        self.search_btn().click()
