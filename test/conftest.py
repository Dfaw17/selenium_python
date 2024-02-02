from selenium import webdriver
import pytest
from helper.config import *


@pytest.fixture()
def open_driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    open_driver.get(url_web)
    yield
    open_driver.quit()


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # BEFORE SUITE

    yield
    # AFTER SUITE
