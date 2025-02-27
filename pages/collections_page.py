"""from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

    def navigate_collection(self):
        self.driver.get("https://alpha-app.backstract.io/workspace/work_e0468da2bbc64c7cbaa65b3954b7ad5b?name=students%20management%20system")

    def add_collecction(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_collection-btn"))).click()

    def close_alert_updrage_plan(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "close_alert_updrage_plan"))
            )
            close_button.click()
            print("Cancel' button clicked successfully.")
        except Exception as e:
            print("Error: Could not click 'Cancel' button:", e)

    def click_on_add_collection(self, collection_name, collection_desc):
        self.driver.find_element(By.ID, "create_col-name-input").send_keys(collection_name)
        self.driver.find_element(By.ID, "create_col-desc-input").send_keys(collection_desc)
        # Wait and click on the dropdown input field to open the dropdown
        input_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select environment']"))
        )
        input_field.click()  # This clicks on the dropdown

        # Now select the 'Python' option from the dropdown
        python_button = self.driver.find_element(By.XPATH, "//button[@id='collection_lan_type-python']")
        python_button.click()  # This clicks the 'Python' option

        # Optionally: Add assertion to verify the selection if needed
        selected_value = input_field.get_attribute('value')



"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WorkspacePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        """Navigate to the workspace page."""
        self.driver.get("https://alpha-app.backstract.io/workspace")

    def enter_workspace_name(self, workspace_name):
        """Enter workspace name in the input field."""
        workspace_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "workspace_enter_input"))
        )
        workspace_input.clear()
        workspace_input.send_keys(workspace_name)

    def click_workspace_button(self):
        """Click the button to create a workspace."""
        self.driver.find_element(By.ID, "create_workspace_btn").click()

    def click_workspace_name(self):
        """Click on the first workspace name and return the new URL dynamically."""
        workspace_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "workspace_card_0"))
        )
        workspace_button.click()
        time.sleep(3)  # Give time for the page to load

        # Extract the new URL dynamically
        workspace_url = self.driver.current_url
        print("Extracted Workspace URL:", workspace_url)
        return workspace_url

    def add_workspace_card(self):
        """Click to add a new workspace card."""
        self.driver.find_element(By.ID, "add_workspace_card").click()

    def add_collection(self):
        """Click the 'Add Collection' button."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add_collecction-btn"))
        ).click()

        time.sleep(5)

        # Extract the new collection URL
        collection_url = self.driver.current_url
        print("Extracted Collection URL:", collection_url)
        return collection_url


    def click_on_add_collection(self, collection_name, collection_desc,):
        """Fill out the add collection form."""
        self.driver.find_element(By.ID, "create_col-name-input").send_keys(collection_name)
        self.driver.find_element(By.ID, "create_col-desc-input").send_keys(collection_desc)

        # Wait and click on the dropdown to select environment
        input_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select environment']"))
        )
        input_field.click()

        # Select 'Python' from the dropdown
        python_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='collection_lan_type-python']"))
        )
        python_button.click()

        print("Collection created with Python environment.")

        self.driver.find_element(By.ID, "create_col-next-btn").click()

    def create_a_datasource(self, url, username, port, password):
        self.driver.find_element(By.CSS_SELECTOR, "svg.Accordion_toggle__mjVLm")
        time.sleep(5)
        self.driver.find_element(By.ID, "import_db_url-input").send_keys(url)
        self.driver.find_element(By.ID, "import_db_username-input").send_keys(username)
        self.driver.find_element(By.ID, "import_db_port-input").send_keys(port)
        self.driver.find_element(By.ID, "import_db_passowrd-input").send_keys(password)


    def close_alert_upgrade_plan(self):
            """Close the upgrade plan alert if it appears."""
            try:
                close_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "close_alert_updrage_plan"))
                )
                close_button.click()
                print("Upgrade plan alert closed successfully.")
            except Exception:
                print("No upgrade plan alert found.")
