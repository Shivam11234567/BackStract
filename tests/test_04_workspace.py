import pytest
import time
from pages.login_page import LoginPage
from pages.workspace_page import WorkspacePage


@pytest.mark.usefixtures("driver")
class TestDashboard:

    # Test Cases1
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

        dashboard.create_a_datasource("aws-0-ap-southeast-1.pooler.supabase.com", "postgres.wdgdermffpbfpwlmivau",
                                      "5432", "$hivam+9988")
        print("Create a datasource successfully")

        time.sleep(15)
        print("pass1 the test")

        dashboard.select_postgres_database(driver)
        time.sleep(10)
        print("Select Postgres database")

    # Test Cases4
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

        get_collection_url = dashboard.run_debug()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", get_collection_url)
        time.sleep(10)

        driver.get(get_collection_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.run_debug()
        print("'run and debug' Click successfully")
        time.sleep(10)

        dashboard.run()
        print("clicked run button successfully")
        time.sleep(10)

        dashboard.publish()
        print("Publish Button clicked Successfully")
        time.sleep(60)

        dashboard.go_to_dashboard()
        print("Go TO Dashboard Button CLicked Succesfully and Deployed Succesfully Done")
        time.sleep(30)

        """go_to_dashboard_url = dashboard.go_to_dashboard()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", go_to_dashboard_url)
        time.sleep(30)

        driver.get(go_to_dashboard_url)  # Navigate to the extracted collection URL
        time.sleep(10)"""

    # Test Cases5
    def test_with_get_api(self, driver):
        print("clicked collections successfully")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

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

        created_collection_get_url = dashboard.get_api_1()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", created_collection_get_url)
        time.sleep(10)

        driver.get(created_collection_get_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.get_api()
        print("Clicked 'get api' click successfully")
        time.sleep(10)

        get_collection_url = dashboard.run_debug()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", get_collection_url)
        time.sleep(10)

        driver.get(get_collection_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.run_debug()
        print("'run and debug' Click successfully")
        time.sleep(10)

        dashboard.run()
        print("clicked run button successfully")
        time.sleep(10)

        dashboard.publish()
        print("Publish Button clicked Successfully")
        time.sleep(60)

        dashboard.go_to_dashboard()
        print("Go TO Dashboard Button CLicked Succesfully and Deployed Succesfully Done")
        time.sleep(30)

    # Test Cases6
    def test_with_post_api(self, driver):
        print("clicked collections successfully")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

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

        created_collection_post_url = dashboard.post_api()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", created_collection_post_url)
        time.sleep(10)

        driver.get(created_collection_post_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.post_api()
        print("Clicked 'get api' click successfully")
        time.sleep(10)

        get_collection_url = dashboard.run_debug()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", get_collection_url)
        time.sleep(10)

        driver.get(get_collection_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.run_debug()
        print("'run and debug' Click successfully")
        time.sleep(10)

        dashboard.run()
        print("clicked run button successfully")
        time.sleep(10)

        dashboard.publish()
        print("Publish Button clicked Successfully")
        time.sleep(60)

        dashboard.go_to_dashboard()
        print("Go TO Dashboard Button CLicked Succesfully and Deployed Succesfully Done")
        time.sleep(30)

    # Test Cases7
    def test_with_put_api(self, driver):
        print("clicked collections successfully")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

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

        created_collection_put_url = dashboard.put_api()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", created_collection_put_url)
        time.sleep(10)

        driver.get(created_collection_put_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.put_api()
        print("Clicked 'get api' click successfully")
        time.sleep(10)

        get_collection_url = dashboard.run_debug()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", get_collection_url)
        time.sleep(10)

        driver.get(get_collection_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.run_debug()
        print("'run and debug' Click successfully")
        time.sleep(10)

        dashboard.run()
        print("clicked run button successfully")
        time.sleep(10)

        dashboard.publish()
        print("Publish Button clicked Successfully")
        time.sleep(60)

        dashboard.go_to_dashboard()
        print("Go TO Dashboard Button CLicked Succesfully and Deployed Succesfully Done")
        time.sleep(30)

    # Test Cases8
    def test_with_delete_api(self, driver):
        print("clicked collections successfully")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

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

        created_collection_delete_url = dashboard.delete_api()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", created_collection_delete_url)
        time.sleep(10)

        driver.get(created_collection_delete_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.delete_api()
        print("Clicked 'get api' click successfully")
        time.sleep(10)

        get_collection_url = dashboard.run_debug()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", get_collection_url)
        time.sleep(10)

        driver.get(get_collection_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.run_debug()
        print("'run and debug' Click successfully")
        time.sleep(10)

        dashboard.run()
        print("clicked run button successfully")
        time.sleep(10)

        dashboard.publish()
        print("Publish Button clicked Successfully")
        time.sleep(60)

        dashboard.go_to_dashboard()
        print("Go TO Dashboard Button CLicked Succesfully and Deployed Succesfully Done")
        time.sleep(30)

    """def test_with_workspace_setting(self, driver):

        print("clicked collections successfully")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

        dashboard = WorkspacePage(driver)
        print("navigate to workspace setting")




        dashboard.navigate()
        workspace_setting_url = dashboard.workspace_setting()  # Extracts the URL dynamically
        print("Navigated to extracted workspace URL:", workspace_setting_url)
        time.sleep(10)

        driver.get(workspace_setting_url)  # Navigate to the extracted workspace URL
        time.sleep(10)"""

    # Test Cases9
    def test_with_post_api_input(self, driver):
        print("clicked collections successfully")

        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

        # Step 2: Navigate to Workspace
        dashboard = WorkspacePage(driver)
        dashboard.navigate()
        workspace_url = dashboard.click_workspace_name()  # Extracts the URL dynamically
        print("Navigated to extracted workspace URL:", workspace_url)
        time.sleep(10)

        driver.get(workspace_url)  # Navigate to the extracted workspace URL
        time.sleep(10)

        # Step 3: Open Collection
        dashboard.collection1()
        print("Clicked 'Collection' button successfully")
        time.sleep(10)

        # Step 4: Open API Builder
        created_collection_post_url = dashboard.post_api()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", created_collection_post_url)
        time.sleep(10)

        driver.get(created_collection_post_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.post_api()
        print("Clicked 'get api' click successfully")
        time.sleep(10)

        # Step 5:

        dashboard.enter_key_post_api("name")
        print("Enter Keys name' successfully")
        time.sleep(10)
        print("pass the test")

        dashboard.input_add_button()
        print("Input Add Button' successfully")
        time.sleep(10)

    # Test Cases10
    def test_with_put_api_input(self, driver):
        print("clicked collections successfully")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

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

        created_collection_put_url = dashboard.put_api()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", created_collection_put_url)
        time.sleep(10)

        driver.get(created_collection_put_url)  # Navigate to the extracted collection URL
        time.sleep(10)

        dashboard.put_api()
        print("Clicked 'Put api' click successfully")
        time.sleep(10)

        dashboard.raw_delete()
        print("delete the raw data successfully")

        dashboard.enter_key_put_api("name")
        print("Enter Keys name' successfully")
        time.sleep(10)
        print("pass the test")

        dashboard.input_add_button()
        print("Input Add Button' successfully")
        time.sleep(10)

        dashboard.run_debug()
        print("'run and debug' Click successfully")
        time.sleep(10)

        dashboard.run()
        print("clicked run button successfully")
        time.sleep(10)

        dashboard.publish()
        print("Publish Button clicked Successfully")
        time.sleep(60)

        dashboard.go_to_dashboard()
        print("Go TO Dashboard Button CLicked Succesfully and Deployed Succesfully Done")
        time.sleep(30)

    # Test Cases11
    def test_with_post_api_input_add_form_data(self, driver):
        print("clicked collections successfully")
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)

        dashboard = WorkspacePage(driver)
        dashboard.navigate()
        workspace_url = dashboard.click_workspace_name()  # Extracts the URL dynamically
        print("Navigated to extracted workspace URL:", workspace_url)
        time.sleep(5)

        driver.get(workspace_url)  # Navigate to the extracted workspace URL
        time.sleep(5)

        # Step 3: Open Collection
        dashboard.collection1()
        print("Clicked 'Collection' button successfully")
        time.sleep(5)

        # Step 4: Open API Builder
        created_collection_post_url = dashboard.post_api()  # Extracts the URL dynamically
        print("Navigated to extracted collections URL:", created_collection_post_url)
        time.sleep(10)

        driver.get(created_collection_post_url)  # Navigate to the extracted collection URL
        time.sleep(5)

        dashboard.post_api()
        print("Clicked 'post api' click successfully")
        time.sleep(10)

        dashboard.add_form_data_input_field("file_upload")
        print("Clicked 'form data' successfully")
        time.sleep(10)

        print("pass the test")

        """dashboard.input_add_button()
        print("Input Add Button' successfully")
        time.sleep(10)"""

        dashboard.code_block()
        print("Clicked 'code block' successfully")
        time.sleep(10)

        dashboard.run_debug()
        print("'run and debug' Click successfully")
        time.sleep(10)

        dashboard.run()
        print("clicked run button successfully")
        time.sleep(10)

        dashboard.publish()
        print("Publish Button clicked Successfully")
        time.sleep(60)

        dashboard.go_to_dashboard()
        print("Go TO Dashboard Button CLicked Succesfully and Deployed Succesfully Done")
        time.sleep(30)
