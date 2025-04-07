# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="Remote")
    parser.addoption("--remote-url", action="store", default="http://localhost:4444/wd/hub")

@pytest.fixture
def driver(request):
    use_remote = request.config.getoption("--driver") == "Remote"
    if use_remote:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Remote(
            command_executor=request.config.getoption("--remote-url"),
            options=options
        )
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
