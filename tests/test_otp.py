"""import time
import pytest
from pages.otp_page import OTPPage


def test_otp(driver):
    driver.get("https://yopmail.com/")  # Replace with your app's OTP page

    otp_page = OTPPage(driver)
    otp_page.enter_otp("12345")  # Replace with dynamic OTP logic if needed
    otp_page.click_verify()

    time.sleep(2)
"""

"""import time
import pytest
from pages.login_page import otp

@pytest.mark.usefixtures("driver")
class otp:
    def test_correct_otp(self, driver):
        print("Testing with correct otp")
        otp = otp(driver)
        driver.get("https://alpha-app.backstract.io/auth/signup")
        otp.enter_otp("1234")
        otp.click_submit_button()
        time.sleep(4)
"""
import pytest
@pytest.mark.usefixtures("driver")
class OtpTests:
    def test_correct_otp(self, driver):
        print("Testing with correct otp")
        otp_page = OTPPage(driver)  # Corrected class usage
        driver.get("https://alpha-app.backstract.io/auth/signup")
        otp_page.enter_otp("1234")
        otp_page.click_submit_button()
"""class TestDashboard:

    def test_with_valid_workspace_name(self, driver):
        print("Testing login and navigating to dashboard")

        # Step 1: Log in First
        login_page = LoginPage(driver)
        driver.get("https://alpha-app.backstract.io/auth/login")
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

        # Step 2: Navigate to the Dashboard after Login
        dashboard = DashboardPage(driver)
        dashboard.navigate()
        dashboard.enter_workspace_name("Shivam Srivastav")
        dashboard.click_workspace_button()
        time.sleep(4)


        # Step 3: Navigate workspace_name
        dashboard = DashboardPage(driver)
        dashboard.navigate()
        dashboard.click_workspace_name_button()
        time.sleep(4)

        dashboard.DashboardPage()
        dashboard.click_workspace_name_button()
        print("Onboarding completed successfully.")

        # Step 4: Extract the new URL after clicking the button
        new_url = driver.current_url
        print("Current URL after clicking workspace button:", new_url)

        # Assert that the URL has changed
        assert "workspace/work_" in new_url, "URL did not change as expected"""

"""def test_with_valid_workspace_name(self, driver):
        print("Testing login and navigating to dashboard")

        # Step 1: Log in First
        login_page = LoginPage(driver)
        driver.get("https://alpha-app.backstract.io/auth/login")
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

        # Step 2: Navigate to the Dashboard after Login

        dashboard = DashboardPage(driver)
        dashboard.navigate()
        dashboard.enter_workspace_name("Shivam Srivastav")
        dashboard.click_workspace_button()

        time.sleep(10)"""