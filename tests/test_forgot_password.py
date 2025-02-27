"""import time
import pytest
from pages.forgot_password_page import ForgotPasswordPage
from utilities.email_utils import get_otp_from_email


@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    def test_valid_password_reset(self, driver):
        #Test resetting password with a valid OTP and matching passwords.
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
        #Test entering an incorrect OTP.
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()

        time.sleep(10)  # Wait for OTP email
        forgot_password.enter_otp_verification("123456")  # Incorrect OTP


    def test_expired_otp(self, driver):
        #Test entering an expired OTP.
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()

        time.sleep(60)  # Simulate waiting for OTP to expire
        otp = get_otp_from_email()


    def test_mismatched_passwords(self, driver):
        #Test entering mismatched new and confirm password fields.
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
"""

"""import time
import pytest
from pages.forgot_password_page import ForgotPasswordPage
from utilities.email_utils import get_otp_from_email


@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    def test_valid_password_reset(self, driver):
        #Test resetting password with a valid OTP and matching passwords.
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
        #Test entering an incorrect OTP.
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()

        time.sleep(10)  # Wait for OTP email
        forgot_password.enter_otp_verification("123456")  # Incorrect OTP


    def test_expired_otp(self, driver):
        #Test entering an expired OTP.
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()

        time.sleep(60)  # Simulate waiting for OTP to expire
        otp = get_otp_from_email()


    def test_mismatched_passwords(self, driver):
        #Test entering mismatched new and confirm password fields.
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
"""

import time
import pytest
from selenium.webdriver.common.by import By
from pages.forgot_password_page import ForgotPasswordPage
from utilities.email_utils import get_otp_from_email


@pytest.mark.usefixtures("driver")
class TestForgotPassword:
    def test_redirect_forgot_password_page(self, driver):
        """Verify that the 'Forgot Password' link redirects to the correct page."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        assert "forget-password" in driver.current_url, "Failed to navigate to Forgot Password page."

    def test_empty_email_validation(self, driver):
        """Verify email field validation when left empty."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("")
        forgot_password.click_continue()
        # Add assertion for validation message
        time.sleep(3)

    def test_invalid_email_format(self, driver):
        """Verify error message for invalid email format."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("invalidEmail")
        forgot_password.click_continue()
        # Add assertion for invalid email error message
        time.sleep(3)

    def test_valid_email_otp_generation(self, driver):
        """Verify that entering a valid email allows OTP generation."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()
        # Add assertion to verify OTP sent
        time.sleep(10)

    def test_empty_otp_field(self, driver):
        """Verify OTP field validation when left empty."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()
        time.sleep(3)
        otp = get_otp_from_email()
        assert otp, "Failed to retrieve OTP."
        forgot_password.enter_otp_verification("")
        # Add assertion for validation message
        time.sleep(3)

    def test_invalid_otp_entry(self, driver):
        """Verify error message for incorrect OTP entry."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()
        otp = get_otp_from_email()
        assert otp, "Failed to retrieve OTP."
        forgot_password.enter_otp_verification("123456")  # Invalid OTP
        # Add assertion for invalid OTP message
        time.sleep(5)

    def test_valid_otp_entry(self, driver):
        """Verify successful OTP verification with a correct OTP."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()
        time.sleep(10)
        otp = get_otp_from_email()
        assert otp, "Failed to retrieve OTP."
        forgot_password.enter_otp_verification(otp)
        # Add assertion to verify redirection to new password page
        time.sleep(3)

    def test_expired_otp(self, driver):
        """Verify behavior when OTP expires."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()
        time.sleep(60)  # Simulate OTP expiry
        otp = get_otp_from_email()
        forgot_password.enter_otp_verification(otp)
        # Add assertion for expired OTP error message
        time.sleep(3)

    """def test_resend_otp_functionality(self, driver):
        #Verify the functionality of the 'Resend OTP' option.
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("testuser@example.com")
        forgot_password.click_continue()
        time.sleep(10)
        forgot_password.click_resend_otp()
        # Add assertion to verify new OTP sent
        time.sleep(3)"""

    def test_mismatched_passwords(self, driver):
        """Verify error message for mismatched new and confirm password fields."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()
        time.sleep(10)
        otp = get_otp_from_email()
        forgot_password.enter_otp_verification(otp)
        forgot_password.create_new_password("Pass@123", "Pass@321")  # Mismatched passwords
        # Add assertion for mismatched password error message
        time.sleep(3)

    def test_valid_password_reset(self, driver):
        """Verify that a valid new password allows successful reset."""
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.navigate()
        forgot_password.enter_email("shivamtesting7@gmail.com")
        forgot_password.click_continue()
        time.sleep(10)
        otp = get_otp_from_email()
        forgot_password.enter_otp_verification(otp)
        forgot_password.create_new_password("Pass@9988", "Pass@9988")
        # Add assertion to verify redirection to login page
        time.sleep(3)