import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from helper.config import *
from helper.actions import *
from pom.pom_login import *
from helper.step_shared import *


def test_login_normal(open_driver):
    click_elem(open_driver, btn_login)
    input_text(open_driver, et_email, "qa2.test@pintu.co.id")
    input_text(open_driver, et_pwd, "Test12345")
    click_elem(open_driver, btn_submit)
    check_display(open_driver, page_auth)
    open_driver.find_element(By.XPATH, "(//input)[1]").send_keys("7")
    open_driver.find_element(By.XPATH, "(//input)[2]").send_keys("7")
    open_driver.find_element(By.XPATH, "(//input)[3]").send_keys("8")
    open_driver.find_element(By.XPATH, "(//input)[4]").send_keys("8")
    open_driver.find_element(By.XPATH, "(//input)[5]").send_keys("9")
    open_driver.find_element(By.XPATH, "(//input)[6]").send_keys("9")
    check_display(open_driver, menu_dashboard)
