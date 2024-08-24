import json
from typing import Tuple, List

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from app.routes import Routes
from app.ui.base.base_page_locators import BasePageLocators


class BasePage:
    url = Routes.BASE_URL
    locators = BasePageLocators()
    actions = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actions = ActionChains(driver)

    @allure.step("Get User Agent")
    def get_user_agent(self):
        user_agent = self.driver.execute_script("return navigator.userAgent;")
        allure.attach(
            body=json.dumps({"User Agent": user_agent}),
            attachment_type=AttachmentType.JSON
        )
        return user_agent

    def open(self):
        with allure.step(f"Open {self.url} page"):
            self.driver.get(self.url)

    def wait(self, timeout=10, poll_frequency=0.5) -> WebDriverWait:
        """
        Basic setup for Explicit Waits
        :param timeout: max time (in seconds to wait for condition
        :param poll_frequency: pause between polls
        :return: WebDriverWait
        """
        if timeout is None:
            timeout = 10
        return WebDriverWait(
            driver=self.driver, timeout=timeout, poll_frequency=poll_frequency
        )

    def is_opened(self):
        with allure.step(f"Page {self.url} is opened"):
            return self.wait().until(EC.url_to_be(self.url))

    def find_element(self, locator: Tuple[str, str], timeout=10) -> WebElement:
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_visible_element(
            self, locator: Tuple[str, str], timeout=10
    ) -> WebElement:
        return self.wait(timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable_element(
            self, locator: Tuple[str, str], timeout=10
    ) -> WebElement:
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def find_elements(
            self, locator: Tuple[str, str], timeout=10
    ) -> List[WebElement]:
        return self.wait(timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def find_visible_elements(
            self, locator: Tuple[str, str], timeout=10
    ) -> List[WebElement]:
        return self.wait(timeout).until(
            EC.visibility_of_any_elements_located(locator)
        )

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG,
        )

    def is_element_present(self, locator: Tuple[str, str], timeout=10) -> bool:
        try:
            self.find_element(locator, timeout)
        except TimeoutException:
            return False
        return True

    def is_not_element_present(
            self, locator: Tuple[str, str], timeout=10
    ) -> bool:
        return not self.is_element_present(locator, timeout)

    def scroll_element_into_view(self, element: WebElement):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element
        )
