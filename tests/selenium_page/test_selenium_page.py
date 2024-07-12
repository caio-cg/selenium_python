import pytest

from pages.selenium.SeleniumPage import SeleniumPage


class TestSeleniumPage:

    @pytest.fixture(scope="function")
    def selenium_page(self, driver):
        return SeleniumPage(driver)

    def test_red_boxes_should_be_displayed_when_the_button_add_to_box_is_clicked(self, selenium_page):
        selenium_page.navigate()
        selenium_page.click_on_add_a_box()

        assert selenium_page.is_the_newest_box_visible()

    def test_invisible_input_should_be_displayed_when_the_reveal_a_new_input_is_clicked(self, selenium_page):
        selenium_page.navigate()
        selenium_page.click_on_reveal_a_new_input()
        selenium_page.wait_for_visibility_of_invisible_input()

        assert selenium_page.is_input_visible()
