from pages.BasePageObject import BasePageObject
from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass(frozen=True)
class _Selectors:
    username_textbox = (By.ID, "user-name")
    password_textbox = (By.ID, "password")
    login_button = (By.ID, "login-button")
    accepted_usernames_container = (By.ID, "login_credentials")
    password_container = (By.CSS_SELECTOR, "div[data-test=login-password]")


class LoginPage(BasePageObject):
    URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        self.driver.get(self.URL)

    def fill_in_username(self, name: str):
        self._fill_in_text(name, _Selectors.username_textbox)

    def fill_in_password(self, password: str):
        self._fill_in_text(password, _Selectors.password_textbox)

    def click_on_login_button(self):
        self._click(_Selectors.login_button)

    def get_accepted_usernames(self) -> list[str]:
        return self._get_inner_text(_Selectors.accepted_usernames_container).splitlines()[1:]

    def get_password(self) -> str:
        return self._get_inner_text(_Selectors.password_container).splitlines()[1:]
