import json
import os
from pathlib import Path

from pytest import fixture
from selenium import webdriver
from config import Config
from utils.logger import Logger

data_path = os.path.join(Path(__file__).absolute().parent.parent, 'data', 'test_data.json')


def driver(browser):
    web_drivers = {
        'chrome': webdriver.Chrome,
        'firefox': webdriver.Firefox
    }
    if browser.lower() not in web_drivers.keys():
        raise Exception(f'{browser} is not supported browsers (supported browsers: {web_drivers.keys()})')
    Logger().log().info(f'Launch {browser} browser')
    web_driver = web_drivers[browser]()
    web_driver.implicitly_wait(10)  # seconds
    return web_driver


def pytest_addoption(parser):
    # If browser is not set in cmd Chrome will be used by default
    parser.addoption("--browser", default="chrome")


@fixture()
def browser(request):
    return request.config.getoption("--browser")


@fixture()
def setup(browser):
    web_driver = driver(browser)
    web_driver.get(Config('qa').base_url)
    yield web_driver
    web_driver.close()


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(data_path))
def test_data(request):
    data = request.param
    return data
