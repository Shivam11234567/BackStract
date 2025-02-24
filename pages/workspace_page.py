from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WorkspacePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://alpha-app.backstract.io/workspace")

    def enter_workspace_name(self, workspace_name):
        # Wait until the input field is clickable
        workspace_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "workspace_enter_input"))
        )
        workspace_input.clear()  # Clear any existing text
        workspace_input.send_keys(workspace_name)

    def click_workspace_button(self):
            self.driver.find_element(By.ID, "create_workspace_btn").click()

    def navigate_workspace(self):
        self.driver.get("https://alpha-app.backstract.io/workspace")

    def click_workspace_name(self):
        workspace_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "workspace_card_0"))
        )
        workspace_button.click()

    def add_workspace_card(self):
        self.driver.find_element(By.ID, "add_workspace_card").click()

    def close_alert_updrage_plan(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "close_alert_updrage_plan"))
            )
            close_button.click()
            print("✅ 'Cancel' button clicked successfully.")
        except Exception as e:
            print("🚨 Error: Could not click 'Cancel' button:", e)





