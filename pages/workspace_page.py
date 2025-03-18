from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
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

    def click_workspace_setting_button(self):
            """Click the button to workspace Setting Button."""
            self.driver.find_element(By.ID, "workspace_card_setting_0").click()

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
        self.driver.find_element(By.CSS_SELECTOR, "svg.Accordion_toggle__mjVLm").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "import_db_url-input").send_keys(url)
        self.driver.find_element(By.ID, "import_db_username-input").send_keys(username)
        self.driver.find_element(By.ID, "import_db_port-input").send_keys(port)
        self.driver.find_element(By.ID, "import_db_passowrd-input").send_keys(password)

        # Click on the SSL dropdown to open the options
        ssl_dropdown = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "css-1xc3v61-indicatorContainer"))
        )
        ssl_dropdown.click()

        # Select "True" from the dropdown
        true_option = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(text(),'True')]")
            )
        )
        true_option.click()
        print("selected true")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "test_db_connection-btn"))
        ).click()

    def select_postgres_database(self, driver):



        # Click on the database dropdown
        database_dropdown = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "import_db-list"))
        )
        print("Database dropdown found.")
        database_dropdown.click()

        #Select "Postgres" from the dropdown
        postgres_option = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='postgres']"))
        )
        postgres_option.click()
        print("Successfully selected 'Postgres' from the database dropdown.")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "import_db_continue-btn"))
        ).click()


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

            # Extract the new URL dynamically
            collection_url = self.driver.current_url
            print("Extracted collection URL:", collection_url)
            return collection_url

    def collection1(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "collection__card--0"))
        ).click()

    def get_api(self):
        api_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "api__card-0"))
        )
        api_element.click()

        # Extract the new collection URL
        created_collection1_url = self.driver.current_url
        print("Extracted Collection URL:", created_collection1_url)
        return created_collection1_url

    """def get_copy_endpoint(self):
        copy_endpoint = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "copy_endpoint_link"))
        )
        copy_endpoint.click()

    def delete_collection(self):
        delete_api = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "delete_endpoint_action"))
        )
        delete_api.click()"""

    def run_debug(self):
        run_debug = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "header_run_and_debug"))
        )
        run_debug.click()

        #Extract the get api builder screen

        get_collection_url = self.driver.current_url
        print("Extracted Collection URL:", get_collection_url)
        return get_collection_url

    print("test")

    def run(self):
            run = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "builde_sidebar_run_btn"))
            )
            run.click()

    def publish(self):
            publish = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.ID, "header_publish"))
            )
            publish.click()


    def go_to_dashboard(self):
        go_to_dashboard = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "col_go_to_dashboard"))
        )
        go_to_dashboard.click()

        #Extract the Go to Dashboard screen

        """go_to_dashboard_url = self.driver.current_url
        print("Extracted Collection URL:", go_to_dashboard_url)
        return go_to_dashboard_url"""


    def get_api_1(self):
        post_api = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "api__card-1"))
        )
        post_api.click()

        # Extract the new collection URL
        created_collection_get_url = self.driver.current_url
        print("Extracted Collection URL:", created_collection_get_url)
        return created_collection_get_url

    def post_api(self):
        post_api = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "api__card-2"))
        )
        post_api.click()

        # Extract the new collection URL
        created_collection_post_url = self.driver.current_url
        print("Extracted Collection URL:", created_collection_post_url)
        return created_collection_post_url

    def put_api(self):
        put_api = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "api__card-3"))
        )
        put_api.click()

        # Extract the new collection URL
        created_collection_put_url = self.driver.current_url
        print("Extracted Collection URL:", created_collection_put_url)
        return created_collection_put_url

    def delete_api(self):
            delete_api = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "api__card-4"))
            )
            delete_api.click()

            # Extract the new collection URL
            created_collection_delete_url = self.driver.current_url
            print("Extracted Collection URL:", created_collection_delete_url)
            return created_collection_delete_url


    """def workspace_setting(self):
            workspace_setting = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "workspace_card_setting_0"))
            )
            workspace_setting.click()

            # Extract the new collection URL
            workspace_setting_url = self.driver.current_url
            print("Extracted Collection URL:", workspace_setting_url)
            return workspace_setting_url"""

    """def post_api_input_raw(self):
        post_api = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "body_raw_0_input"))


        )
        post_api.click()

        # Extract the new collection URL
        created_collection_post_url = self.driver.current_url
        print("Extracted Collection URL:", created_collection_post_url)
        return created_collection_post_url"""


    def enter_key_post_api(self, key):

            """self.driver.find_element(By.ID, "builder_add_input_block").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "builder_sidebar_param_0").click()
            time.sleep(5)"""

            self.driver.find_element(By.ID, "param_expand").click()
            time.sleep(3)

            # Wait for the input field to be clickable
            workspace_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "param_3_input"))
            )
            workspace_input.clear()
            workspace_input.send_keys(key)

            # ID selector
            datatype_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "param_0_select_clickable"))
            )
            datatype_dropdown.click()

            # wait for the option to be clickable
            string_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "param_0_select_option_0"))
            )
            string_button.click()

            print("Test successful")




    def enter_key_put_api(self, key):

            """self.driver.find_element(By.ID, "param_expand").click()
            time.sleep(3)"""

            # Wait for the input field to be clickable
            workspace_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "param_3_input"))
            )
            workspace_input.clear()
            workspace_input.send_keys(key)

            # ID selector
            datatype_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "param_3_select_clickable"))
            )
            datatype_dropdown.click()

            # wait for the option to be clickable
            string_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "param_3_select_option_0"))
            )
            string_button.click()

            print("Test successful")

    def input_add_button(self):
            input_add_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "sidebar_btn_continue"))
            )
            input_add_button.click()

    def  param_delete(self):
        param_delete = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "body_raw_0_delete"))
            )
        param_delete.click()

        self.driver.find_element(By.ID, "modal_right-btn").click()

    def raw_delete(self):
        raw_delete = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "body_raw_delete"))
            )
        raw_delete.click()

        self.driver.find_element(By.ID, "modal_left-btn").click()


    def add_form_data_input_field(self, key):

        self.driver.find_element(By.ID, "builder_add_input_block").click()

        form_data = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "builder_sidebar_body_0"))
        )
        form_data.click()

        # Wait for the input field to be clickable
        workspace_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "body_formData_0_input"))
        )
        workspace_input.clear()
        workspace_input.send_keys(key)

        # ID selector
        datatype_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "body_formData_0_select_clickable"))
        )
        datatype_dropdown.click()

        # wait for the option to be clickable
        string_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "body_formData_0_select_option_1"))
        )
        string_button.click()

        """self.driver.find_element(By.ID, "sidebar_btn_continue").click()"""

        continue_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sidebar_btn_continue"))
        )
        continue_button.click()

        """self.driver.find_element(By.XPATH, "//button[contains(@class, 'Button_btn__zZlFC')]").click()"""

    def code_block(self):
            code_block = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_btn__zZlFC')]"))
            )
            code_block.click()

    def function_block_btn(self):

        code_block_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "function_block_btn"))
        )
        code_block_button.click()


    def file_upload(self):
        file_upload_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Upload A File']"))
        )
        file_upload_dropdown.click()

        # wait for the option to be clickable
        file_upload_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Upload A File')]"))
        )
        file_upload_button.click()

    def database_requests(self):
        database_requests = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h2[contains(text(), 'database requests')]"))
        )
        database_requests.click()

    def query_get_a_record(self):
        query_get_a_record = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Query Get a Record')]"))
        )
        query_get_a_record.click()

    def choose_table(self):
        choose_table = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h3[contains(text(), 'students')]"))
        )
        choose_table.click()

    def query_get_a_record_student(self):
        try:
            # Print the current URL for debugging
            print("Current URL:", self.driver.current_url)

            # Wait for the element to be visible
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "your_locator"))
            )
            print("Element found:", element.text)

        except TimeoutException:
            # Print the page source and take a screenshot for debugging
            print("Page source:", self.driver.page_source)
            self.driver.save_screenshot("timeout_error.png")
            raise TimeoutException("Element not found within the specified time")

        except StaleElementReferenceException:
            # Re-locate the element if it becomes stale
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "your_locator"))
            )
            print("Re-located element:", element.text)

