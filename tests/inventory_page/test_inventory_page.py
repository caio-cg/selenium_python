import pytest

from pages.inventory.InventoryPage import InventoryPage
from pages.login.LoginPage import LoginPage


@pytest.fixture(autouse=True, scope="function")
def set_user_session(driver):
    driver.get(LoginPage.URL)
    driver.add_cookie({"name": "session-username", "value": "standard_user"})


@pytest.fixture(scope="function")
def inventory_page(driver):
    return InventoryPage(driver)


def test_inventory_page_should_list_all_products(inventory_page):
    inventory_page.navigate()
    product_names = inventory_page.get_all_product_names()

    assert len(product_names) > 0


def test_inventory_page_should_list_all_products_fully(inventory_page):
    inventory_page.navigate()
    products = inventory_page.get_all_products()

    assert len(products) > 0, "At least one product should be listed on screen"

    for product in products:
        assert product.get_price(), "Price should not be empty"
        assert product.get_product_name(), "Product name should not be empty"
        assert product.get_product_description(), "Product description should not be empty"
