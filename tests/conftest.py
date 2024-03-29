import json
import os
from pathlib import Path

import allure
from pytest import fixture
from config import Config
from utils.driver import Driver
from utils.logger import Logger

data_path = os.path.join(Path(__file__).absolute().parent.parent, 'data', 'test_data.json')


def pytest_addoption(parser):
    # If browser is not set in cmd Chrome will be used by default
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", default="False")


@fixture()
def parameters(request):
    Logger().log().info(f'Test name: {request.node.name}')
    return {'browser': request.config.getoption("--browser"),
            'headless': request.config.getoption("--headless")}


@fixture()
def setup(parameters, request):
    try:
        web_driver = Driver(parameters['browser'], eval(parameters['headless'])).get_browser()
    except NameError:
        raise Exception("'--headless' parameter must be True or False")
    web_driver.get(Config('qa').base_url)
    yield web_driver
    # Take a screenshot if test failed
    if request.session.testsfailed:
        allure.attach(
            web_driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
    web_driver.close()


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(data_path))
def test_data(request):
    data = request.param
    return data
