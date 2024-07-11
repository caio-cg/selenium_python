from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePageObject import BasePageObject


class BaseComponent(BasePageObject):

    def __init__(self, driver, web_element: WebElement):
        super().__init__(driver)
        self.wait = WebDriverWait(driver=web_element, timeout=4, poll_frequency=0.2)

    def navigate(self):
        raise Exception("Components are not navigable")
