import pytest
import time
from pages.login_page import LoginPage
from pages.workspace_page import WorkspacePage


@pytest.mark.usefixtures("driver")
class TestDashboard:

    #Test Cases1
    def test_with_valid_workspace_name(self, driver):
        """Test creating a workspace with a valid name."""
        print("Testing login and navigating to dashboard")

        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)
        driver.refresh()

        dashboard = WorkspacePage(driver)
        dashboard.navigate()
        dashboard.enter_workspace_name("students management system")
        print("Workspace name created successfully")
        dashboard.click_workspace_button()

        time.sleep(5)


    # Test Cases2
    def test_add_workspace_card(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()
        time.sleep(4)

        dashboard = WorkspacePage(driver)
        dashboard.navigate()
        dashboard.add_workspace_card()
        print("Workspace card added navigated successfully.")
        time.sleep(5)

        dashboard = WorkspacePage(driver)
        dashboard.navigate()
        dashboard.close_alert_upgrade_plan()
        print("Workspace cancel successfully.")
        time.sleep(5)

    # Test Cases3
    def test_create_collections(self, driver):

        print("Testing login and navigating to dashboard")

        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)
        driver.refresh()

        dashboard = WorkspacePage(driver)
        dashboard.navigate()
        workspace_url = dashboard.click_workspace_name()  # Extracts the URL dynamically
        print("Navigated to extracted workspace URL:", workspace_url)
        time.sleep(10)

        driver.get(workspace_url)  # Navigate to the extracted workspace URL
        time.sleep(10)

        dashboard.add_collection()
        print("Clicked 'Add Collection' button successfully")
        time.sleep(10)

        dashboard.click_on_add_collection("Students Collection", "test")
        print("Add Collection name' successfully")
        time.sleep(10)
        print("pass the test")

        dashboard.create_a_datasource("aws-0-ap-southeast-1.pooler.supabase.com", "postgres.wdgdermffpbfpwlmivau","5432", "$hivam+9988")
        print("Create a datasource successfully")

        time.sleep(15)
        print("pass1 the test")

        dashboard.select_postgres_database(driver)
        time.sleep(10)
        print("Select Postgres database")

    def test_collections(self, driver):

        print("clicked collections successfully")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)
        driver.refresh()

        dashboard = WorkspacePage(driver)
        dashboard.navigate()
        workspace_url = dashboard.click_workspace_name()  # Extracts the URL dynamically
        print("Navigated to extracted workspace URL:", workspace_url)
        time.sleep(10)

        driver.get(workspace_url)  # Navigate to the extracted workspace URL
        time.sleep(10)

        dashboard.collection1()
        print("Clicked 'Collection' button successfully")
        time.sleep(10)

        created_collection1_url = dashboard.get_api()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", created_collection1_url)
        time.sleep(10)

        driver.get(created_collection1_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.get_api()
        print("Clicked 'get api' click successfully")
        time.sleep(10)


        """dashboard.get_copy_endpoint()
        print("Copy 'get copy endpoint' successfully")

        dashboard.delete_collection()
        print("click delete Button successfully")"""

        print("test")
        get_collection_url = dashboard.run_debug()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", get_collection_url)
        time.sleep(10)

        driver.get(get_collection_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.run_debug()
        print("'run and debug' Click successfully")
        time.sleep(10)


