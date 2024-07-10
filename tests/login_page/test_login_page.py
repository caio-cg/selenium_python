from pages.inventory.InventoryPage import InventoryPage
from pages.login.LoginPage import LoginPage
import pytest

login_page: LoginPage
accepted_usernames: list[str]
password: str


@pytest.fixture(autouse=True, scope="function")
def setup(driver):
    print("BEGINNING SETUP")
    global login_page
    login_page = LoginPage(driver)

    login_page.navigate()
    global accepted_usernames
    accepted_usernames = login_page.get_accepted_usernames()
    global password
    password = login_page.get_password()
    yield password
    print("FINISHING SETUP")


def test_valid_user_should_be_able_to_log_in(driver):
    login_page.fill_in_username(accepted_usernames[0])
    login_page.fill_in_password(password)
    login_page.click_on_login_button()

    login_page.wait_until_url_to_be(InventoryPage.URL)

    assert driver.title == "Swag Labs"


def test_locked_our_user_should_not_be_able_to_log_in(driver):
    login_page.fill_in_username(accepted_usernames[1])
    login_page.fill_in_password(password)
    login_page.click_on_login_button()

    login_page.wait_until_url_to_be(InventoryPage.URL)

    assert driver.title == "Swag Labs"
