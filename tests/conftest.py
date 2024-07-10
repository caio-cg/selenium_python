import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope="function")
def driver():
    print("Creating new driver instance")
    driver = webdriver.Chrome()
    yield driver
    print("Closing driver")
    driver.quit()
