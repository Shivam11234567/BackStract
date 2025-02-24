import pytest
import time
from pages.login_page import LoginPage
from pages.workspace_page import WorkspacePage


@pytest.mark.usefixtures("driver")
class TestDashboard:
    def test_with_valid_workspace_name(self, driver):
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
        dashboard.enter_workspace_name("Shivam Srivastava")
        dashboard.click_workspace_button()

        time.sleep(5)
        driver.refresh()

        dashboard.navigate_workspace()
        dashboard.click_workspace_name()
        print("Onboarding completed successfully.")

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