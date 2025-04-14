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



    def code_block_file_upload(self):
        code_block_file_upload_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_1"))
        )
        print("file upload dropdown found.")
        code_block_file_upload_dropdown.click()

        file_upload_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Upload A File']"))
        )
        file_upload_code_block.click()

    def upload_a_file_cloud_existing_variable(self):
        existing_variable_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_storage_type"))
        )
        print("Existing Variable (Type: file)dropdown found.")
        existing_variable_dropdown.click()

        existing_variable_select = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs_storage_type__form_data--file_upload"))
        )
        existing_variable_select.click()

    def return_value_upload_a_file(self):
        return_value_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_storage_return_value"))
        )
        print("Existing Variable (Type: file)dropdown found.")
        return_value_dropdown.click()

        return_value_select = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs_storage_return_value__file--file_url"))
        )
        return_value_select.click()

    def upload_a_file_return_as(self,field_value):
        return_as_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "fs_file_var"))
        )
        return_as_input.clear()
        return_as_input.send_keys(field_value)



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
         table_column_keys_dropdown = WebDriverWait(self.driver, 15).until(
             EC.element_to_be_clickable((By.ID, "table__col__key"))
         )
         print("Table Column Key dropdown found.")
         table_column_keys_dropdown.click()

         id_option = WebDriverWait(self.driver, 15).until(
             EC.element_to_be_clickable((By.CLASS_NAME, "table__col__key--id"))
         )
         id_option.click()
         print("Successfully selected 'id_option' from the Table column keys dropdown.")

    def field_value(self):

        field_value_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "field__value__select"))
        )
        print("Field Value dropdown found.")
        field_value_dropdown.click()

        field_value_code_block = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "field__value__select--code_block-students_edited_record-id"))
        )
        field_value_code_block.click()


    def return_as_input(self, field_value):
        """Enter field value in the return as field."""
        return_as_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "return__var__input"))
        )
        return_as_input.clear()
        return_as_input.send_keys(field_value)

    def comment_input(self, field_value):
        """Enter comment in the comment field."""
        comment_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "block__comment__input"))
        )
        comment_input.clear()
        comment_input.send_keys(field_value)

    def btn__add(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "btn__add__fs"))
        ).click()

    def output_block_btn(self):
        output_block_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "output_block_btn"))
        )
        output_block_btn.click()

    def add_output_return_value_dropdown(self):
        return_value_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__output"))
        )
        print("return value dropdown found.")
        return_value_dropdown.click()

        select_return_value = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__output--code_block-student"))
        )
        select_return_value.click()

        print("Successfully selected 'select_return_value' from the return value dropdown.")

    def add_output_add_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "continue__btn"))
        ).click()

    def output_return_as_input(self, field_value):
        """Enter field value in the return as field."""
        return_as_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fs__return__as"))
        )
        return_as_input.clear()
        return_as_input.send_keys(field_value)

    def query_has_a_record(self):
        query_has_a_record = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Query Has a Record')]"))
        )
        query_has_a_record.click()


    def has_a_record_field_value(self):

        field_value_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__field__value__input"))
        )
        print("Field Value dropdown found.")
        field_value_dropdown.click()

        field_value_code_block = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "fs__field__value__input--code_block-student-id"))
        )
        field_value_code_block.click()

    def query_has_a_record_student(self):

        table_column_keys_dropdown = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "table__column__select"))
        )
        print("Table Column Key dropdown found.")
        table_column_keys_dropdown.click()

        id_option = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "table__column__select--id"))
        )
        id_option.click()
        print("Successfully selected 'id_option' from the Table column keys dropdown.")


    def has_a_record_return_as_input(self, field_value):
        """Enter field value in the return as field."""
        return_as_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fs__return__var"))
        )
        return_as_input.clear()
        return_as_input.send_keys(field_value)

    def has_a_record_comment_input(self, field_value):
        """Enter comment in the comment field."""
        comment_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fs__block_comment"))
        )
        comment_input.clear()
        comment_input.send_keys(field_value)

    def has_a_record_btn__add(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "fs__add__btn"))
        ).click()

    def query_get_all_record(self):
        query_get_all_record = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Query Get all Record')]"))
        )
        query_get_all_record.click()

    def query_get_all_record_student(self):

        table_column_keys_dropdown = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "table__column__select"))
        )
        print("Table Column Key dropdown found.")
        table_column_keys_dropdown.click()

        id_option = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "table__column__select--id"))
        )
        id_option.click()
        print("Successfully selected 'id_option' from the Table column keys dropdown.")

    def get_all_record_field_value(self):

        field_value_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__field__value"))
        )
        print("Field Value dropdown found.")
        field_value_dropdown.click()

        field_value_code_block = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "fs__field__value--code_block-student-id"))
        )
        field_value_code_block.click()

    def get_all_record_sort(self):
        get_all_record_sort_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "sort__fs__input"))
        )
        print("sort dropdown found.")
        get_all_record_sort_dropdown.click()

        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and text()='Ascending']"))
        )
        option.click()

    def get_all_record_return_as_input(self, field_value):
        """Enter field value in the return as field."""
        return_as_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fs__return__var_input"))
        )
        return_as_input.clear()
        return_as_input.send_keys(field_value)

    def get_all_record_comment_input(self, field_value):
        """Enter comment in the comment field."""
        comment_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fs__block__comment__input"))
        )
        comment_input.clear()
        comment_input.send_keys(field_value)


    def get_all_record_btn__add(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "btn__add__fs"))
        ).click()

    def query_add_record(self):
        query_add_record = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Query Get all Record')]"))
        )
        query_add_record.click()

    def query_add_record_student(self):

        table_column_keys_dropdown = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "table__column__select"))
        )
        print("Table Column Key dropdown found.")
        table_column_keys_dropdown.click()

        id_option = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "table__column__key--id"))
        )
        id_option.click()
        print("Successfully selected 'id_option' from the Table column keys dropdown.")

    def builder_add_input_block(self):
        self.driver.find_element(By.ID, "builder_add_input_block").click()
        time.sleep(3)

    def code_block_function_block_btn(self):
        self.driver.find_element(By.ID, "function_block_btn").click()
        time.sleep(3)

    def code_block_data_manipulations(self):
        code_block_data_manipulations_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_3"))
        )
        print("file upload dropdown found.")
        code_block_data_manipulations_dropdown.click()

        data_manipulations_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Create a new variable']"))
        )
        data_manipulations_code_block.click()

    def create_a_new_variable_input_var_name(self,field_value):
        value_name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "fs__var-name"))
        )
        value_name_input.clear()
        value_name_input.send_keys(field_value)

    def data_manipulations_var_type(self):
        code_block_var_type_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-type"))
        )
        print("file upload dropdown found.")
        code_block_var_type_dropdown.click()

        var_type_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-type--any"))
        )
        var_type_code_block.click()

    def data_manipulations_field_type(self):
        field_type_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-value"))
        )
        print("Field Value dropdown found.")
        field_type_dropdown.click()

        field_type_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-value--query-id"))
        )
        field_type_code_block.click()

    def data_manipulations_add_btn(self):
        create_var_add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "fs__add_block"))
        )
        create_var_add_btn.click()


    def code_block_data_manipulations_update_a_variable(self):
        code_block_data_manipulations_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_3"))
        )
        print("clicked")
        code_block_data_manipulations_dropdown.click()

        data_manipulations_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Update a variable']"))
        )
        data_manipulations_code_block.click()

    def code_block_data_manipulations_existing_variable(self):
        existing_variable_data_manipulations_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-existing"))
        )
        print("clicked")
        existing_variable_data_manipulations_dropdown.click()

        data_manipulations_existing_variable = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "fs__var-existing--query-id"))
        )
        data_manipulations_existing_variable.click()

    def data_manipulations_update_a_variable_field_value(self):
        field_type_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-value"))
        )
        print("clicked")
        field_type_dropdown.click()

        field_type_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-value--query-user"))
        )
        field_type_code_block.click()

    def code_block_data_manipulations_create_a_new_list(self):
        code_block_data_manipulations_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_3"))
        )
        print("clicked")
        code_block_data_manipulations_dropdown.click()

        data_manipulations_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Create a new list/dictionary']"))
        )
        data_manipulations_code_block.click()


    def code_block_data_manipulations_create_a_new_list_list(self):
        container_type_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-type"))
        )
        print("file upload dropdown found.")
        container_type_dropdown.click()

        container_type_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-type--list"))
        )
        container_type_code_block.click()

    def code_block_data_manipulations_create_a_new_list_dictionary(self):
        container_type_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-type"))
        )
        print("file upload dropdown found.")
        container_type_dropdown.click()

        container_type_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-type--dictionary"))
        )
        container_type_code_block.click()

    def var_name(self,field_value):
        value_name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "fs__var-name"))
        )
        value_name_input.clear()
        value_name_input.send_keys(field_value)

    def data_manipulations_create_a_new_list_var_type(self):
        create_a_new_list_var_type_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-data-type"))
        )
        print("file upload dropdown found.")
        create_a_new_list_var_type_dropdown.click()

        create_a_new_list_var_type = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-data-type--any"))
        )
        create_a_new_list_var_type.click()

    def code_block_data_list_add_element_at_start(self):
        code_block_list_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_7"))
        )
        print("list button clicked successful")
        code_block_list_dropdown.click()

        # selecting "Query Add Record"
        add_record_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Add element at start/end']"))
        )
        add_record_option.click()

    def code_block_data_add_element_at_start_option(self):
        var_operation_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-operation"))
        )
        print("Variable operation dropdown found.")
        var_operation_dropdown.click()

        option_text  = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-operation--start"))
        )
        option_text .click()

    def code_block_list_existing_variable(self):
        existing_variable_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-exiting"))
        )
        print("Existing variable dropdown found and clicked")
        existing_variable_dropdown.click()

        selected_option  = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-exiting--code_block-user_list"))
        )
        selected_option .click()

    def code_block_list_var_type(self):
        list_var_type = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-type"))
        )
        print("Existing variable dropdown found and clicked")
        list_var_type.click()

        selected_option  = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-type--any"))
        )
        selected_option .click()

    def code_block_list_value(self):
        list_value = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-value"))
        )
        print("Existing variable dropdown found and clicked")
        list_value.click()

        selected_option  = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-value--query-id"))
        )
        selected_option .click()

    def code_block_data_list_remove_element_at_start(self):
        code_block_list_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_7"))
        )
        print("list button clicked successful")
        code_block_list_dropdown.click()

        # selecting "Query Add Record"
        remove_element_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Remove element at start/end']"))
        )
        remove_element_option.click()

    def code_block_list_remove_element_at_start_existing_variable(self):
        existing_variable_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-existing"))
        )
        print("Existing variable dropdown found and clicked")
        existing_variable_dropdown.click()

        selected_option  = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-existing--code_block-user_list"))
        )
        selected_option .click()

    def code_block_data_list_get_element_at_index(self):
        code_block_list_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_7"))
        )
        print("list button clicked successful")
        code_block_list_dropdown.click()

        # selecting "Query Add Record"
        selected_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Get element at index']"))
        )
        selected_option.click()

    def code_block_list_get_element_at_index(self):
        existing_variable_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-exiting"))
        )
        print("Existing variable dropdown found and clicked")
        existing_variable_dropdown.click()

        selected_option  = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-exiting--code_block-user_list"))
        )
        selected_option .click()

    def code_block_list_get_element_at_index_at_index(self, field_value):
        """Enter comment in the comment field."""
        at_index_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fs__var-index-at"))
        )
        at_index_input.clear()
        at_index_input.send_keys(field_value)

    def code_block_list_get_element_at_index_return_value_as(self):
        return_value_as_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-return"))
        )
        print("Existing variable dropdown found and clicked")
        return_value_as_dropdown.click()

        selected_option  = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-return--code_block-user_list"))
        )
        selected_option .click()

    def code_block_data_list_update_element_at_index(self):
        code_block_list_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_7"))
        )
        print("list button clicked successful")
        code_block_list_dropdown.click()

        # selecting "Query Add Record"
        selected_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Update element at index']"))
        )
        selected_option.click()

    def code_block_data_list_update_element_at_index_value(self):
        field_type_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-value"))
        )
        print("clicked")
        field_type_dropdown.click()

        field_type_code_block = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-value--query-user"))
        )
        field_type_code_block.click()

    def code_block_data_list_get_length(self):
        code_block_list_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_7"))
        )
        print("list button clicked successful")
        code_block_list_dropdown.click()

        # selecting "Query Add Record"
        selected_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Get length']"))
        )
        selected_option.click()

    def code_block_list_get_length_value_as(self):
        return_value_as_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs__var-return"))
        )
        print("Existing variable dropdown found and clicked")
        return_value_as_dropdown.click()

        selected_option  = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fs__var-return--code_block-students_edited_record-id"))
        )
        selected_option .click()

    def code_block_data_list_empty_an_list(self):
        code_block_list_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_7"))
        )
        print("list button clicked successful")
        code_block_list_dropdown.click()

        # selecting "Query Add Record"
        selected_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Empty an List']"))
        )
        selected_option.click()

    def code_block_data_list_empty_an_list_bool(self):
        code_block_list_dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "fs_cat_7"))
        )
        print("list button clicked successful")
        code_block_list_dropdown.click()

        # selecting "Query Add Record"
        selected_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='Element in List(Bool)']"))
        )
        selected_option.click()