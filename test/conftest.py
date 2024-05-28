from selenium import webdriver
import pytest
from helper.config import *
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def open_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
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
