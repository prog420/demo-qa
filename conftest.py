import logging
import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

pytest_plugins = (
    "utils.fixtures.report",
)

logger = logging.getLogger("test")


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--headless", action="store_true")
    parser.addoption("--ignore-passed-test-attachments", action="store_true")
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="session")
def base_temp_directory(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """
    Get base temporary directory which can be changed via --basetemp="<dir>".

    If test run was launched from Gitlab (check predefined CI_BUILDS_DIR var),
    return shared volume between Selenium service and main container
    """
    # "/tmp/downloads" for Selenium Grid
    if os.getenv("CI_BUILDS_DIR"):
        return Path("/builds")
    else:
        return tmp_path_factory.getbasetemp()


@pytest.fixture(scope="session")
def config(request: pytest.FixtureRequest):
    headless = request.config.getoption("--headless")
    browser = request.config.getoption("--browser")
    ignore_passed_test_attachments = request.config.getoption("--ignore-passed-test-attachments")

    if browser.lower() == "chrome":
        options = ChromeOptions()
        # Install ad block extension
        options.add_extension(
            "resources/extensions/uBlock0_1.52.0.chromium.zip"
        )
    else:
        raise ValueError(f"Browser {browser} is not supported.")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if headless:
        options.add_argument("--headless=new")

    return {
        "headless": headless,
        "browser": browser,
        "options": options,
        "ignore_passed_test_attachments": ignore_passed_test_attachments
    }


@pytest.fixture(scope="function")
def driver(config):
    driver = None

    if config["browser"].lower() == "chrome":
        driver = webdriver.Chrome(
            options=config["options"], service=ChromeService()
        )

    yield driver
    if driver is not None:
        driver.close()
        driver.quit()
