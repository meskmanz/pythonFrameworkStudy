from selenium.webdriver.common.by import By


class HomePage:
    _logo_xpath = '//img[@class="img-fluid"]'
    _search_form_xpath = '//div[@id="search"]'
    _search_textfield_xpath = f'{_search_form_xpath}/input'
    _search_btn_xpath = f'{_search_form_xpath}/span/button'

    def __init__(self, driver):
        self.driver = driver

    # Elements

    def logo_img(self):
        return self.driver.find_element(By.XPATH, self._logo_xpath)

    def search_text_field(self):
        return self.driver.find_element(By.XPATH, self._search_textfield_xpath)

    def search_btn(self):
        return self.driver.find_element(By.XPATH, self._search_btn_xpath)

    # Business Logic

    def search(self, text):
        self.search_text_field().send_keys(text)
        self.search_btn().click()
