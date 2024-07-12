from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import abstractmethod
from typing import Tuple


class BasePageObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=4, poll_frequency=0.2)

    @abstractmethod
    def navigate(self):
        pass

    def wait_until_url_to_be(self, url: str):
        self.wait.until(EC.url_to_be(url))

    def _click(self, element: WebElement):
        # self.wait.until(lambda d: element.is_enabled() and element.is_displayed())
        self.wait.until(EC.element_to_be_clickable(element),
                        "Element is not enabled or displayed to be clicked")
        element.click()

    def _click(self, locator_type_and_selector: Tuple[str, str]):
        element: WebElement = self.wait.until(EC.presence_of_element_located(locator_type_and_selector)
                                              and EC.element_to_be_clickable(locator_type_and_selector),
                                              f"Element with locator '{locator_type_and_selector[1]}' could not be clicked")
        element.click()

    def _fill_in_text(self, text: str, locator_type_and_selector: Tuple[str, str]):
        element: WebElement = self.wait.until(EC.presence_of_element_located(locator_type_and_selector)
                                              and EC.element_to_be_clickable(locator_type_and_selector),
                                              f"Element with locator '{locator_type_and_selector[1]}' could not be filled in with text '{text}'")
        element.clear()
        element.send_keys(text)

    def _get_inner_text(self, locator_type_and_selector: Tuple[str, str]):
        element: WebElement = self.wait.until(EC.presence_of_element_located(locator_type_and_selector)
                                              and EC.visibility_of_element_located(locator_type_and_selector),
                                              f"Element with locator '{locator_type_and_selector[1]}' is not visible")
        return element.text

    def _is_displayed(self, locator_type_and_selector: Tuple[str, str]) -> bool:
        element: WebElement = self.wait.until(EC.presence_of_element_located(locator_type_and_selector),
                                              f"Element with locator '{locator_type_and_selector[1]}' is not visible")
        return element.is_displayed()

    def _wait_visibility_of(self, locator_type_and_selector: Tuple[str, str]):
        self.wait.until(EC.presence_of_element_located(locator_type_and_selector)
                        and EC.visibility_of_element_located(locator_type_and_selector),
                        f"Element with locator '{locator_type_and_selector[1]}' is not visible")
