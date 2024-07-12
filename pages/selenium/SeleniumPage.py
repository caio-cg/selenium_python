from dataclasses import dataclass

from selenium.webdriver.common.by import By

from pages.BasePageObject import BasePageObject


@dataclass(frozen=True)
class _Selectors:
    add_button = (By.ID, "adder")
    reveal_input_button = (By.ID, "reveal")
    invisible_input = (By.ID, "revealed")


class SeleniumPage(BasePageObject):
    URL = "https://www.selenium.dev/selenium/web/dynamic.html"

    def __init__(self, driver):
        super().__init__(driver)
        self._click_counter = -1

    def navigate(self):
        self._click_counter = -1
        self.driver.get(self.URL)

    def click_on_add_a_box(self):
        self._click(_Selectors.add_button)
        self._click_counter += 1

    def click_on_reveal_a_new_input(self):
        self._click(_Selectors.reveal_input_button)

    def is_the_newest_box_visible(self) -> bool:
        return self._is_displayed((By.ID, f"box{self._click_counter}"))

    def is_input_visible(self) -> bool:
        return self._is_displayed(_Selectors.invisible_input)

    def wait_for_visibility_of_invisible_input(self):
        self._wait_visibility_of(_Selectors.invisible_input)
