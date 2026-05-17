import base64
import os

import pytest
import pytest_html

from drivers.driver_factory import DriverFactory
from utilities.json_helper import JsonHelper
from utilities.logger_helper import LoggerHelper
from utilities.screenshot_helper import ScreenshotHelper

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


@pytest.fixture(scope="function")
def driver(browser, config):
    logger.info(f"Launching The {browser} Browser")
    driver = DriverFactory.get_driver(browser)
    url = config["base_url"]
    driver.get(url)
    logger.info(f"Launched The {url} URL")
    yield driver
    DriverFactory.quit_driver()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            file_path = ScreenshotHelper.take_screenshot(driver, item.name)
            with open(file_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode()

            # attach screenshot to the report
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.png(encoded_image))
            report.extra = extra
