import time
import pytest
from pages.signup_page import SignupPage
from utilities.email_utils import get_otp_from_email

@pytest.mark.usefixtures("driver")
class TestSignup:
    def test_signup_and_onboarding(self, driver):
        print("Testing signup and onboarding process")
        signup = SignupPage(driver)

        # Navigate to Signup Page
        signup.navigate()
        signup.enter_name_and_continue("Shivam Srivastava")
        signup.fill_email_and_password("shivamtesting7@gmail.com", "Pass@9988", "Pass@9988")

        time.sleep(15)  # Wait for OTP email
        otp = get_otp_from_email()

        if otp:
            signup.enter_otp(otp)
            print(f"OTP entered: {otp}")
        else:
            print("Failed to retrieve OTP")
            return

        time.sleep(5)

        # Navigate to Onboarding Page and complete steps
        signup.navigate_to_onboarding()
        signup.select_role()
        print("Onboarding completed successfully.")

        signup.navigate_to_onboarding()
        signup.select_role1()
        print("Onboarding completed successfully.")

        signup.navigate_to_onboarding()
        signup.select_role2()
        print("Onboarding completed successfully.")

        # Navigate to Onboarding pricing page
        signup.navigate_to_onboarding_pricing()
        signup.select_price()
        print("Onboarding completed successfully.")

    def test_signup_with_invalid_email(self, driver):
        print("Testing signup with invalid email")
        signup = SignupPage(driver)

        signup.navigate()
        signup.enter_name_and_continue("Shivam Srivastava")
        signup.fill_email_and_password("abcdgmail.com", "Pass@9988", "Pass@9988")

        time.sleep(3)

    def test_signup_with_mismatched_passwords(self, driver):
        print("Testing signup with mismatched passwords")
        signup = SignupPage(driver)

        signup.navigate()
        signup.enter_name_and_continue("Shivam Srivastava")
        signup.fill_email_and_password("xyz@yopmail.com", "Pass@9988", "WrongPassword")

        time.sleep(3)

    def test_signup_with_registered_email(self, driver):
        print("Testing signup with an already registered email")
        signup = SignupPage(driver)

        signup.navigate()
        signup.enter_name_and_continue("Shivam Srivastava")
        signup.fill_email_and_password("shivamtesting7@gmail.com", "Pass@9988", "Pass@9988")

        time.sleep(3)

    def test_signup_with_invalid_otp(self, driver):
        print("Testing signup with an invalid OTP")
        signup = SignupPage(driver)

        signup.navigate()
        signup.enter_name_and_continue("Shivam Srivastava")
        signup.fill_email_and_password("shivam@yopmail.com", "Pass@9988", "Pass@9988")

        time.sleep(5)
        signup.enter_otp("123456")  # Entering an invalid OTP

        time.sleep(3)

    def test_signup_with_empty_fields(self, driver):
        print("Testing signup with empty fields")
        signup = SignupPage(driver)

        signup.navigate()
        signup.enter_name_and_continue("")  # Empty name
        signup.fill_email_and_password("", "", "")  # Empty email and password fields

        time.sleep(3)

    def test_signup_with_expired_otp(self, driver):
        print("Testing signup with an expired OTP")
        signup = SignupPage(driver)

        signup.navigate()
        signup.enter_name_and_continue("Shivam Srivastava")
        signup.fill_email_and_password("shivam@yopmail.com", "Pass@9988", "Pass@9988")

        time.sleep(300)
        otp = get_otp_from_email()

        if otp:
            signup.enter_otp(otp)
            print(f"Expired OTP entered: {otp}")
        else:
            print("Failed to retrieve OTP")

        time.sleep(3)
