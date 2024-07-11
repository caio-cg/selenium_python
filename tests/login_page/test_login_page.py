from pages.inventory.InventoryPage import InventoryPage
from pages.login.LoginPage import LoginPage
from typing import Tuple
import pytest


@pytest.fixture(autouse=True, scope="function")
def login_page(driver):
    return LoginPage(driver)


def _get_credentials_from_page(login_page: LoginPage) -> Tuple:
    accepted_usernames = login_page.get_accepted_usernames()
    password = login_page.get_password()

    assert len(accepted_usernames) > 0, "the user's list should not be empty"
    assert password, "the password should not be empty"

    return accepted_usernames, password


def test_valid_user_should_be_able_to_log_in(driver, login_page: LoginPage):
    login_page.navigate()
    (accepted_usernames, password) = _get_credentials_from_page(login_page)

    assert accepted_usernames[0] == "standard_user", "user should be 'standard_user'"

    login_page.fill_in_username(accepted_usernames[0])
    login_page.fill_in_password(password)
    login_page.click_on_login_button()

    login_page.wait_until_url_to_be(InventoryPage.URL)

    assert driver.title == "Swag Labs"


_data_provider_invalid_users = [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("unknown_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
]


@pytest.mark.parametrize("username, password, expected_message", _data_provider_invalid_users)
def test_invalid_users_should_not_be_able_to_log_in(driver, login_page: LoginPage, username: str, password: str,
                                                    expected_message: str):
    login_page.navigate()

    login_page.fill_in_username(username)
    login_page.fill_in_password(password)
    login_page.click_on_login_button()

    assert login_page.is_error_message_displayed(), "error message should be displayed"
    assert login_page.get_error_message() == expected_message


_data_provider_erratic_users = [
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
]


@pytest.mark.parametrize("username", _data_provider_erratic_users)
def test_erratic_users_should_be_able_to_log_in(driver, login_page: LoginPage, username: str):
    login_page.navigate()

    login_page.fill_in_username(username)
    login_page.fill_in_password("secret_sauce")
    login_page.click_on_login_button()

    login_page.wait_until_url_to_be(InventoryPage.URL)

    assert driver.title == "Swag Labs"
