from selenium.webdriver.common.by import By

btn_login = [By.XPATH, "//*[text()='Log In']"]
et_email = [By.XPATH, "(//input)[1]"]
et_pwd = [By.XPATH, "(//input)[2]"]
btn_submit = [By.XPATH, "//button[@type='submit']"]
page_auth = [By.XPATH, "//h1[text()='Google Authenticator Code']"]
input_auth = [By.XPATH, "//div[@class='gap-2']"]
menu_dashboard = [By.XPATH, "//p[text()='Dashboard']"]
