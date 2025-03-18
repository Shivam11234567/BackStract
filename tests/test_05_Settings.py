import pytest
import time

from pages.Settings_page import SettingsPage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestSettings:

    #Test Cases1
    def test_settings_account_page(self, driver):
        #Test updating profile settings.

        print("Logging in and navigating to dashboard...")

        # Login Steps
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)
        driver.refresh()

        # Navigating to Settings
        settings = SettingsPage(driver)
        settings.navigate_settings()
        print("Clicked Settings Button")
        settings.click_settings()
        time.sleep(5)

        # Updating Profile Name
        settings.enter_profile_name("Shivam Srivastava")
        print("Profile name updated successfully")
        settings.click_save_button()  # Ensure this method exists in `SettingsPage`

    def test_settings_billings_page(self, driver):
        print("test_settings_billings_page")

        # Login Steps
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)
        driver.refresh()

        # Navigating to Settings
        settings = SettingsPage(driver)
        settings.navigate_settings()
        print("Clicked Settings Button")
        settings.settings_billings()
        time.sleep(5)

    def test_settings_purchase_history_page_receipt(self, driver):
        print("test_settings_purchase_history_page")

        # Login Steps
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

        # Navigating to Settings
        settings = SettingsPage(driver)
        settings.navigate_settings()
        print("Clicked Settings Button")
        settings.settings_purchase_history()
        time.sleep(5)

        settings.receipt()
        print("Clicked Receipt Button")


    def test_settings_purchase_history_page_invoice(self, driver):
        print("test_settings_purchase_history_page")

        # Login Steps
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

        # Navigating to Settings
        settings = SettingsPage(driver)
        settings.navigate_settings()
        print("Clicked Settings Button")
        settings.settings_purchase_history()
        time.sleep(5)

        settings.invoice()
        print("Clicked Invoice Button")

