"""from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.ID, "email_input").send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password_input").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login_submit_btn").click()
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://alpha-app.backstract.io/auth/login")

    def enter_email(self, email):
        self.driver.find_element(By.ID, "email_input").send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password_input").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login_submit_btn").click()

    def wait_for_redirect(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_changes("https://alpha-app.backstract.io/auth/login"))