from pages.BasePageObject import BasePageObject
from selenium.webdriver.common.by import By
from dataclasses import dataclass

from pages.inventory.ProductComponent import ProductComponent


@dataclass(frozen=True)
class _Selectors:
    product_names = (By.CSS_SELECTOR, "div[data-test=inventory-item-name]")
    inventory_items = (By.CSS_SELECTOR, "div[data-test=inventory-item]")


class InventoryPage(BasePageObject):
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        self.driver.get(self.URL)

    def get_all_product_names(self) -> list[str]:
        elements = self.driver.find_elements(by=_Selectors.product_names[0], value=_Selectors.product_names[1])
        return [element.text for element in elements]

    def get_all_products(self) -> list[ProductComponent]:
        elements = self.driver.find_elements(by=_Selectors.inventory_items[0], value=_Selectors.inventory_items[1])
        return [ProductComponent(element) for element in elements]
