from pages.BasePageObject import BasePageObject
from selenium.webdriver.common.by import By
from dataclasses import dataclass


class InventoryPage(BasePageObject):
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        self.driver.get(self.URL)
