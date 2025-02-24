
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SignupPage:
    def __init__(self, driver):
        self.SKIP_BUTTON = None
        self.ROLE_SELECTION = None
        self.driver = driver

    def navigate(self):
        self.driver.get("https://alpha-app.backstract.io/auth/signup")

    def enter_name_and_continue(self, name):
        self.driver.find_element(By.ID, "username_input").send_keys(name)
        self.driver.find_element(By.ID, "username__continue").click()
        time.sleep(2)

    def fill_email_and_password(self, email, password, re_password):
        self.driver.find_element(By.ID, "email_input").send_keys(email)
        self.driver.find_element(By.ID, "input_password").send_keys(password)
        self.driver.find_element(By.ID, "input_repassword").send_keys(re_password)
        self.driver.find_element(By.ID, "signup__continue").click()
        time.sleep(2)

    def enter_otp(self, otp):
        #self.driver.find_element(By.ID, "otp_input").send_keys(otp)
        self.driver.find_element(By.XPATH, "//input[@id='otp_input']").send_keys(otp)
        self.driver.find_element(By.ID, "verify_continue").click()
        #self.driver.find_element(By.ID, "otp_submit_button").click()
        time.sleep(10)

        # Navigate to Onboarding Page

    def navigate_to_onboarding(self):
        self.driver.get("https://alpha-app.backstract.io/onboarding")
        time.sleep(3)

    def select_role(self):
        self.driver.find_element(By.CSS_SELECTOR, "#step_0_oboadring_question_0").click()
        time.sleep(2)

    def select_role1(self):
        self.driver.find_element(By.CSS_SELECTOR, "#step_1_oboadring_question_0").click()
        time.sleep(2)

    def select_role2(self):
        self.driver.find_element(By.CSS_SELECTOR, "#step_2_oboadring_question_0").click()
        time.sleep(2)

    # Navigate to Onboarding Page

    def navigate_to_onboarding_pricing(self):
        self.driver.get("https://alpha-app.backstract.io/pricing?from=onboarding")
        time.sleep(1)

    def select_price(self):
        self.driver.find_element(By.CSS_SELECTOR, "#plan_btn_0").click()
        time.sleep(2)
