"""import pytest
import time
from pages.login_page import LoginPage
from pages.workspace_page import WorkspacePage"""


"""@pytest.mark.usefixtures("driver")
class TestDashboard:"""

"""def test_with_valid_workspace_name(self, driver):
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
        print("workspace name created successfully")
        dashboard.click_workspace_button()

        time.sleep(5)
        driver.refresh()

        dashboard.navigate_workspace()
        dashboard.click_workspace_name()
        print("click workspace name button successfully")
        time.sleep(5)

        dashboard.navigate_collection()
        dashboard.add_collecction()
        print ("click add collections button successfully")
        time.sleep(5)


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
        dashboard.close_alert_updrage_plan()
        print("Workspace cancel successfully.")
        time.sleep(5)

    def test_create_collections(self, driver):
        print("Testing login and navigating to dashboard")

        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.enter_email("shivamtesting7@gmail.com")
        login_page.enter_password("Pass@9988")
        login_page.click_login_button()

        time.sleep(4)
        driver.refresh()

        dashboard = WorkspacePage(driver)                               #create
        dashboard.navigate()
        dashboard.enter_workspace_name("students management system")
        print("workspace name created successfully")
        dashboard.click_workspace_button()

        time.sleep(5)
        driver.refresh()

        dashboard.navigate_workspace()                                    #click created workspace name
        dashboard.click_workspace_name()
        print("click workspace name button successfully")
        time.sleep(5)

        dashboard.navigate_collection()                                    #click add collections button
        dashboard.add_collecction()
        print ("click add collections button successfully")
        time.sleep(5)

        dashboard.navigate_collection()
        dashboard.click_on_add_collection()
        print("click on add collection button successfully")"""

""" def test_create_collections(self, driver):
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

        dashboard.create_a_datasource("URL", "test", "postgres", "5432")
        print("Create a datasource successfully")
        time.sleep(10)
        print("pass the test")"""