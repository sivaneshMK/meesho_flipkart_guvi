import pytest

from drivers.driver_factory import DriverFactory
from utilities.json_helper import JsonHelper
from utilities.logger_helper import LoggerHelper

logger = LoggerHelper.get_logger()

# pytest --env=test -m regression --html==report/report.html --self-contained-html

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default="test",
                     help="Environment setup")

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    logger.info(f"Running The Test In {env} Environment")
    return JsonHelper.get_config(env)

@pytest.fixture(scope="session")
def browser(config):
    browser = config["browser"]
    return browser


@pytest.fixture(scope="class")
def driver(browser, config):
    logger.info(f"Launching The {browser} Browser")
    driver = DriverFactory.get_driver(browser)
    url = config["base_url"]
    driver.get(url)
    logger.info(f"Launched The {url} URL")
    yield driver
    DriverFactory.quit_driver()