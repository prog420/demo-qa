import pytest

from selenium.webdriver.remote.webdriver import WebDriver


class BaseCase:
    driver: WebDriver = None
    config = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config
