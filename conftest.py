"""import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
"""


import pytest
from selenium import webdriver
import os

# Fixture to initialize and tear down the WebDriver
@pytest.fixture
def driver():
    #Fixture to initialize and tear down the WebDriver.
    driver = webdriver.Chrome() # Initialize Chrome WebDriver
    driver.maximize_window()    # Maximize the browser window
    yield driver                # Provide the driver to the test
    driver.quit()               # Quit the driver after the test