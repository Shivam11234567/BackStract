"""import time
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_correct_email(self, driver):
        print("Testing with correct email")
        login_page = LoginPage(driver)
        driver.get("https://alpha-app.backstract.io/auth/login")
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(4)

    def test_incorrect_email(self, driver):
        print("Testing with incorrect email")
        login_page = LoginPage(driver)
        driver.get("https://alpha-app.backstract.io/auth/login")
        login_page.enter_email("shivamtesting@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(4)

    def test_incorrect_password(self, driver):
        print("Testing with incorrect password")
        login_page = LoginPage(driver)
        driver.get("https://alpha-app.backstract.io/auth/login")
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("12345")
        login_page.click_login_button()
        time.sleep(4)

    def test_empty_fields(self, driver):
        print("Testing with empty fields")
        login_page = LoginPage(driver)
        driver.get("https://alpha-app.backstract.io/auth/login")
        login_page.enter_email("")
        login_page.enter_password("")
        login_page.click_login_button()
        time.sleep(4)

    def test_invalid_email_format(self, driver):
        print("Testing with invalid email format")
        login_page = LoginPage(driver)
        driver.get("https://alpha-app.backstract.io/auth/login")
        login_page.enter_email("shivamtesting7gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(4)

    def test_redirect_after_login(self, driver):
        print("Testing redirect after login")
        login_page = LoginPage(driver)
        driver.get("https://alpha-app.backstract.io/auth/login")
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(4)

"""

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

    def test_incorrect_email(self, driver):
        """Verify login with incorrect email."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(3)  # Verify the error message manually

    def test_incorrect_password(self, driver):
        """Verify login with incorrect password."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("wrongpassword")
        login_page.click_login_button()
        time.sleep(3)

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

    """def test_google_login(self, driver):
        #Verify login with Google authentication.
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.click_google_login()
        time.sleep(10)"""

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
