from helper.actions import *
from helper.config import *
from pom.pom_login import *


def STEP_login_valid(open_driver):
    input_text(open_driver, et_username, username_valid)
    input_text(open_driver, et_pwd, pwd_valid)
    click_elem(open_driver, btn_login)
    check_display(open_driver, icon_cart)