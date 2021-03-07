from pytest import fixture
from config import Config

from selenium import webdriver
import json

def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        default='dev',
        help='environment to run test'
    )

@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(scope='session')
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()

@fixture(params = [webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def all_browser(request):
    driver = request.param
    drvr = driver()
    yield drvr

    drvr.quit()


@fixture(params = ['Sony_2', 'Sumsong_2'])
def tv_brand_2(request):
    brand = request.param
    return brand



def load_test_data(path):
    with open(path) as f:
        data = json.load(f)
        return data


@fixture(params = load_test_data('test_data.json'))
def tv_brand_3(request):
    brand = request.param
    return brand
