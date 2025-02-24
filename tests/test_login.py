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
        print("Testing with correct email")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        login_page.wait_for_redirect()

    def test_incorrect_email(self, driver):
        print("Testing with incorrect email")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(4)

    def test_incorrect_password(self, driver):
        print("Testing with incorrect password")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("12345")
        login_page.click_login_button()
        time.sleep(4)

    def test_empty_fields(self, driver):
        print("Testing with empty fields")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("")
        login_page.enter_password("")
        login_page.click_login_button()
        time.sleep(4)

    def test_invalid_email_format(self, driver):
        print("Testing with invalid email format")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(4)

    def test_redirect_after_login(self, driver):
        print("Testing redirect after login")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        login_page.wait_for_redirect()
