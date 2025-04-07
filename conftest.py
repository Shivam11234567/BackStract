import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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

    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="Local")
    parser.addoption("--remote-url", action="store", default="http://localhost:4444/wd/hub")
