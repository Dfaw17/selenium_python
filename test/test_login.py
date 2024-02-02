import time
from helper.config import *
from helper.actions import *
from pom.pom_login import *
from helper.step_shared import *


def test_login_normal(open_driver):
    input_text(open_driver, et_username, username_valid)
    input_text(open_driver, et_pwd, pwd_valid)
    click_elem(open_driver, btn_login)
    check_display(open_driver, icon_cart)


def test_logout_normal(open_driver):
    STEP_login_valid(open_driver)
    click_elem(open_driver, hamburger_menu)
    wait(1)
    click_elem(open_driver, btn_logout)
    check_display(open_driver, btn_login)