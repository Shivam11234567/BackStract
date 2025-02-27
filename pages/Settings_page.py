

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_settings(self):
        #Navigate to the Settings page.
        self.driver.get("https://alpha-app.backstract.io/settings/accounts")

    def click_settings(self):

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "settings"))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "settings_accounts"))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "account_edit_btn"))
        ).click()

    def enter_profile_name(self, name):
            """Enter a new profile name."""
            profile_name_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "account_name_input"))
            )
            profile_name_input.clear()
            profile_name_input.send_keys(name)

    def click_save_button(self):
        """Click the Save Changes button to confirm profile updates."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "account_save_changes_btn"))
        ).click()

    def settings_billings(self):
        #Click the Billings Button.
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "settings_billings"))
        ).click()

    def settings_purchase_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "settings_purchase_history"))
        ).click()



