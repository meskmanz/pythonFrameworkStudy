from selenium.webdriver.common.by import By

from components.top_menu_component import TopMenuComponent
from pages.base_page import BasePage


class HomePage(BasePage):
    __logo_xpath = (By.XPATH, '//div[@id="logo"]/a/img')
    __search_form_xpath = (By.XPATH, '//div[@id="search"]')
    __search_textfield_xpath = (By.XPATH, f'{__search_form_xpath[1]}/input')
    __search_btn_xpath = (By.XPATH, f'{__search_form_xpath[1]}/span/button')
    __result_label_xpath = (By.XPATH, '//div[@id="content"]/h1')

    def __init__(self, driver):
        super().__init__(driver)
        self.top_menu = TopMenuComponent(driver)

    # Elements

    def logo_img(self):
        return self.find_element(self.__logo_xpath)

    def search_text_field(self):
        return self.find_element(self.__search_textfield_xpath)

    def search_btn(self):
        return self.find_element(self.__search_btn_xpath)

    def result_label(self):
        return self.find_element(self.__result_label_xpath)

    # Business Logic

    def search(self, text):
        self.log.info(f'Do search for: {text}')
        self.search_text_field().send_keys(text)
        self.search_btn().click()
