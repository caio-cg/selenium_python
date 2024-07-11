from selenium.webdriver.remote.webelement import WebElement

from pages.BaseComponent import BaseComponent
from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass(frozen=True)
class _Selectors:
    product_name = (By.CSS_SELECTOR, "div[data-test=inventory-item-name]")
    product_description = (By.CSS_SELECTOR, "div[data-test=inventory-item-desc]")
    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    price = (By.CSS_SELECTOR, "div[data-test=inventory-item-price]")


class ProductComponent(BaseComponent):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element.parent, web_element)

    def get_price(self) -> str:
        return self._get_inner_text(_Selectors.price)

    def click_add_to_cart(self):
        return self._click(_Selectors.add_to_cart_button)

    def get_product_name(self):
        return self._get_inner_text(_Selectors.product_name)

    def get_product_description(self):
        return self._get_inner_text(_Selectors.product_description)
