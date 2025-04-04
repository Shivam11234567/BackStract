import pytest
from pages.login_page import LoginPage
import time


@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_correct_email(self, driver):
        """Verify login with correct email and password."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        login_page.wait_for_redirect()
        assert "workspace" in driver.current_url, "Login failed with correct credentials"

    def test_incorrect_email(self, driver):
        """Verify login with incorrect email."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        error_message = login_page.get_error_message()
        assert error_message == "user with this email_id does not exists", "Unexpected error message for incorrect email"

    def test_incorrect_password(self, driver):
        """Verify login with incorrect password."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("wrongpassword")
        login_page.click_login_button()
        error_message = login_page.get_error_message()
        assert error_message == "password does not match", "Unexpected error message for incorrect password"

    def test_empty_fields(self, driver):
        """Verify login with empty email and password fields."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("")
        login_page.enter_password("")
        login_page.click_login_button()
        time.sleep(3)

    def test_invalid_email_format(self, driver):
        """Verify login with invalid email format."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(3)

    def test_forgot_password_link(self, driver):
        """Verify the Forgot Password link redirects correctly."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.click_forgot_password()
        assert "forget-password" in driver.current_url, f"Unexpected URL: {driver.current_url}"
        time.sleep(3)

    def test_google_login(self, driver):
        #Verify login with Google authentication.
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.click_google_login()
        time.sleep(10)

    def test_github_login(self, driver):
        """Verify login with GitHub authentication."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.click_github_login()
        time.sleep(3)

    def test_signup_link(self, driver):
        """Verify that clicking Sign Up redirects to the signup page."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.click_signup()
        assert "signup" in driver.current_url  # Check if redirected
        time.sleep(3)

        driver.quit()
