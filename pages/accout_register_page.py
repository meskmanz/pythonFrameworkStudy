from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class AccountRegisterPage(BasePage):
    __firstname_textfield_id = 'input-firstname'
    __lastname_textfield_id = 'input-lastname'
    __email_textfield_id = 'input-email'
    __telephone_textfield_id = 'input-telephone'
    __address_textfield_id = 'input-address-1'
    __city_textfield_id = 'input-city'
    __country_dropdown_id = 'input-country'
    __region_dropdown_id = 'input-zone'
    __password_field_id = 'input-password'
    __confirm_password_field_id = 'input-confirm'
    __agree_checkbox_name = 'agree'
    __submit_btn_xpath = '//input[@type="submit"]'

    # Elements

    def firstname_textfield(self):
        return self.driver.find_element(By.ID, self.__firstname_textfield_id)

    def lastname_textfield(self):
        return self.driver.find_element(By.ID, self.__lastname_textfield_id)

    def email_textfield(self):
        return self.driver.find_element(By.ID, self.__email_textfield_id)

    def telephone_textfield(self):
        return self.driver.find_element(By.ID, self.__telephone_textfield_id)

    def address_textfield(self):
        return self.driver.find_element(By.ID, self.__address_textfield_id)

    def city_textfield(self):
        return self.driver.find_element(By.ID, self.__city_textfield_id)

    def country_dropdown(self):
        return self.driver.find_element(By.ID, self.__country_dropdown_id)

    def region_dropdown(self):
        return self.driver.find_element(By.ID, self.__region_dropdown_id)

    def password_field(self):
        return self.driver.find_element(By.ID, self.__password_field_id)

    def confirm_password_field(self):
        return self.driver.find_element(By.ID, self.__confirm_password_field_id)

    def agree_checkbox(self):
        return self.driver.find_element(By.NAME, self.__agree_checkbox_name)

    def submit_btn(self):
        return self.driver.find_element(By.XPATH, self.__submit_btn_xpath)

    # Business logic

    def fill_the_form(self, firstname=None, lastname=None, email=None, phone=None, address=None, city=None,
                      country=None, region=None, password=None, confirm_password=None, agree=False, submit=False):
        self.log.info('Fill in registration form')
        if firstname is not None:
            self.firstname_textfield().send_keys(firstname)
        if lastname is not None:
            self.lastname_textfield().send_keys(lastname)
        if email is not None:
            self.email_textfield().send_keys(email)
        if phone is not None:
            self.telephone_textfield().send_keys(phone)
        if address is not None:
            self.address_textfield().send_keys(address)
        if city is not None:
            self.city_textfield().send_keys(city)
        if country is not None:
            Select(self.country_dropdown()).select_by_visible_text(country)
        if region is not None:
            Select(self.region_dropdown()).select_by_visible_text(region)
        if password is not None:
            self.password_field().send_keys(password)
        if confirm_password is not None:
            self.confirm_password_field().send_keys(confirm_password)
        if agree:
            self.agree_checkbox().click()
        if submit:
            self.submit_btn().click()
