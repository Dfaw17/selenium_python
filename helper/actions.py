import time

from selenium.webdriver.common.by import By


def click_elem(open_driver, elem):
    open_driver.find_element(elem[0], elem[1]).click()


def input_text(open_driver, elem, text):
    open_driver.find_element(elem[0], elem[1]).send_keys(text)


def wait(sec):
    time.sleep(sec)


def check_display(open_driver, elem):
    open_driver.find_element(elem[0], elem[1]).is_displayed()
