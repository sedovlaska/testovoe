import pytest
from tests.test_selenium.libs.pageobject.mainpage import MainPage1
from tests.test_selenium.libs.locators.mainpage_locators import MainPageLocators
from tests.test_selenium.conftest import BasicSeleniumTest
from tests import constants


@pytest.mark.ui
class TestMainPage1(BasicSeleniumTest):

    @pytest.fixture()
    def _set_up_with_main_page(self):
        main_page = MainPage1(self.driver)
        main_page.go_to_site()
        yield main_page

    def test_button_exist(self, _set_up_with_main_page):
        main_page = _set_up_with_main_page
        main_page.find_element(MainPageLocators.FORM_SEND_BUTTON)

    def test_input_field_exist(self, _set_up_with_main_page):
        main_page = _set_up_with_main_page
        main_page.find_element(MainPageLocators.INPUT_FIELD)

    def test_success_get_info_by_bin(self, _set_up_with_main_page):
        main_page = _set_up_with_main_page
        main_page.enter_value(constants.valid_bank_bin['bin'])
        main_page.click_send_button()
        main_page.check_success_message()
        main_page.check_all_cells_value(constants.valid_bank_bin)

    def test_get_error_message_by_invalid_bin(self, _set_up_with_main_page):
        main_page = _set_up_with_main_page
        main_page.enter_value(constants.invalid_ban_bin['bin'])
        main_page.click_send_button()
        main_page.check_error_message()

    def test_get_data_without_bin(self, _set_up_with_main_page):
        main_page = _set_up_with_main_page
        main_page.click_send_button()
        main_page.check_error_message()
