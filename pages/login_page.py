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

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://alpha-app.backstract.io/auth/login")

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "email_input")
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password_input")
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login_submit_btn").click()

    def wait_for_redirect(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_changes("https://alpha-app.backstract.io/auth/login"))

    def click_forgot_password(self):
        self.driver.find_element(By.ID, "forget__password").click()

    def click_signup(self):
        self.driver.find_element(By.XPATH, "//a[contains(@href, '/auth/signup')]").click()

    def click_google_login(self):
        self.driver.find_element(By.ID, "github_google").click()
        #self.driver.find_element(By.XPATH, "//button[contains(@id, 'google_signup')]").click()

    def click_github_login(self):
        self.driver.find_element(By.ID, "github_signup").click()
