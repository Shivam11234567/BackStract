from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from .locators import LoginLocators

logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        """Navigate to the login page."""
        try:
            self.driver.get("https://alpha-app.backstract.io/auth/login")
            logger.info("Navigated to login page")
        except Exception as e:
            logger.error(f"Failed to navigate to login page: {e}")
            raise

    def enter_email(self, email):
        """Enter email in the email input field."""
        try:
            email_field = self.wait.until(
                EC.element_to_be_clickable(LoginLocators.EMAIL_INPUT)
            )
            email_field.clear()
            email_field.send_keys(email)
            logger.info(f"Entered email: {email}")
        except TimeoutException:
            logger.error("Email input field not found")
            raise

    def enter_password(self, password):
        """Enter password in the password input field."""
        try:
            password_field = self.wait.until(
                EC.element_to_be_clickable(LoginLocators.PASSWORD_INPUT)
            )
            password_field.clear()
            password_field.send_keys(password)
            logger.info("Entered password")
        except TimeoutException:
            logger.error("Password input field not found")
            raise

    def click_login_button(self):
        """Click the login button."""
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)
            )
            login_button.click()
            logger.info("Clicked login button")
        except TimeoutException:
            logger.error("Login button not found")
            raise

    def wait_for_redirect(self, timeout=10):
        """Wait for successful login redirect."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: "workspace" in driver.current_url
            )
            logger.info("Successfully redirected to workspace")
        except TimeoutException:
            logger.error("Login redirect timeout")
            raise

    def click_forgot_password(self):
        """Click the forgot password link."""
        try:
            forgot_password = self.wait.until(
                EC.element_to_be_clickable(LoginLocators.FORGOT_PASSWORD)
            )
            forgot_password.click()
            logger.info("Clicked forgot password link")
        except TimeoutException:
            logger.error("Forgot password link not found")
            raise

    def click_signup(self):
        """Click the signup link."""
        try:
            signup_link = self.wait.until(
                EC.element_to_be_clickable(LoginLocators.SIGNUP_LINK)
            )
            signup_link.click()
            logger.info("Clicked signup link")
        except TimeoutException:
            logger.error("Signup link not found")
            raise

    def click_google_login(self):
        """Click the Google login button."""
        try:
            google_button = self.wait.until(
                EC.element_to_be_clickable(LoginLocators.GOOGLE_LOGIN)
            )
            google_button.click()
            logger.info("Clicked Google login button")
        except TimeoutException:
            logger.error("Google login button not found")
            raise

    def click_github_login(self):
        """Click the GitHub login button."""
        try:
            github_button = self.wait.until(
                EC.element_to_be_clickable(LoginLocators.GITHUB_LOGIN)
            )
            github_button.click()
            logger.info("Clicked GitHub login button")
        except TimeoutException:
            logger.error("GitHub login button not found")
            raise

    def get_error_message(self):
        """Get the error message text if present."""
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE)
            )
            error_text = error_element.text
            logger.info(f"Error message found: {error_text}")
            return error_text
        except TimeoutException:
            logger.debug("No error message found")
            return None
