import pytest
from selenium import webdriver
import os



@pytest.fixture
def driver():
    #Fixture to initialize
    driver = webdriver.Chrome() # Initialize Chrome WebDriver
    driver.maximize_window()    # Maximize the browser window
    yield driver                # Provide the driver to the test
    driver.quit()               # Quit the driver after the test