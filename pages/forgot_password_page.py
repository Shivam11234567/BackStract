"""from selenium.webdriver.common.by import By
import time
class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://alpha-app.backstract.io/auth/forget-password")

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@name='emailId']").send_keys(email)

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//button[@id='forget__continue']").click()

    def enter_otp_verification(self, otp):
        #self.driver.find_element(By.ID, "otp_input").send_keys(otp)
        self.driver.find_element(By.XPATH, "//input[@id='otp_input']").send_keys(otp)
        self.driver.find_element(By.XPATH, "//button[@id='verify_continue']").click()
        #self.driver.find_element(By.ID, "otp_submit_button").click()
        time.sleep(10)

    def test_create_new_password(self, new_password, password_renter_input):
        self.driver.find_element(By.ID, "password_input").send_keys(new_password)
        self.driver.find_element(By.ID, "password_renter_input").send_keys(password_renter_input)
        self.driver.find_element(By.ID, "change__password_continue").click()
        time.sleep(2)
"""

from selenium.webdriver.common.by import By
import time

class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://alpha-app.backstract.io/auth/forget-password")

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@name='emailId']").send_keys(email)

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//button[@id='forget__continue']").click()

    def enter_otp_verification(self, otp):
        self.driver.find_element(By.XPATH, "//input[@id='otp_input']").send_keys(otp)
        self.driver.find_element(By.XPATH, "//button[@id='verify_continue']").click()
        time.sleep(10)

    def create_new_password(self, new_password, confirm_password):
        """Enter new password and confirm password to reset."""
        self.driver.find_element(By.XPATH, "//input[@id='password__input']").send_keys(new_password)
        self.driver.find_element(By.XPATH, "//input[@id='password_renter_input']").send_keys(confirm_password)
        self.driver.find_element(By.ID, "change__password_continue").click()
        time.sleep(2)


