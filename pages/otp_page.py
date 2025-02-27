"""from selenium.webdriver.common.by import By

class OTPPage:
    def __init__(self, driver):
        self.driver = driver
        self.otp_input = (By.XPATH, "//input[@name='login']")
        self.verify_button = (By.XPATH, "//input[@type='submit']")

    def enter_otp(self, otp):
        self.driver.find_element(*self.otp_input).send_keys(otp)

    def click_verify(self):
        self.driver.find_element(*self.verify_button).click()
"""
"""from selenium.webdriver.common.by import By

class otp:
    def __init__(self, driver):
        self.driver = driver

    def enter_OTP(self, otp):
        self.driver.find_element(By.XPATH, "//input[@name='otp']").send_keys(otp)

    def click_submit_button(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()"""



