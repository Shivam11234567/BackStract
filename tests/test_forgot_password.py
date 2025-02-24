import time
import pytest
from pages.forgot_password_page import ForgotPasswordPage
from utilities.email_utils import get_otp_from_email


@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    def test_valid_password_reset(self, driver):
        """Test resetting password with a valid OTP and matching passwords."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()

        time.sleep(10)  # Wait for OTP email
        otp = get_otp_from_email()

        assert otp, "Failed to retrieve OTP."
        forgot_password.enter_otp_verification(otp)
        time.sleep(5)
        forgot_password.create_new_password("Pass@998888", "Pass@998888")
        print("Password reset successful.")
        time.sleep(5)

    def test_invalid_email_format(self, driver):
        print("Testing with invalid email format")
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("Shivam")
        forgot_password.click_continue()
        time.sleep(3)

    def test_empty_email(self, driver):
        print("Testing with empty email")
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("")
        forgot_password.click_continue()
        time.sleep(3)

    def test_incorrect_otp(self, driver):
        """Test entering an incorrect OTP."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()

        time.sleep(10)  # Wait for OTP email
        forgot_password.enter_otp_verification("123456")  # Incorrect OTP


    def test_expired_otp(self, driver):
        """Test entering an expired OTP."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()

        time.sleep(60)  # Simulate waiting for OTP to expire
        otp = get_otp_from_email()


    def test_mismatched_passwords(self, driver):
        """Test entering mismatched new and confirm password fields."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()

        time.sleep(10)  # Wait for OTP email
        otp = get_otp_from_email()

        assert otp, "Failed to retrieve OTP."
        forgot_password.enter_otp_verification(otp)
        time.sleep(5)
        forgot_password.create_new_password("Pass@123456", "Pass@654321")  # Mismatched passwords
