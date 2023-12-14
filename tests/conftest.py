from pytest import fixture
from selenium import webdriver
from config import Config


def driver():
    web_driver = webdriver.Chrome()
    web_driver.implicitly_wait(10)  # seconds
    return web_driver


@fixture(scope='function')
def browser():
    browser = driver()
    browser.get(Config('qa').base_url)
    yield browser
    browser.close()
