import pytest
from tests.test_selenium.libs.selenium_pagefactory_lib.mainpage_2 import MainPage2
from tests.test_selenium.conftest import BasicSeleniumTest
from tests import constants


@pytest.mark.ui
class TestMainPage1(BasicSeleniumTest):

    def test_success_get_info_by_bin(self):
        main_page = MainPage2(self.driver)
        main_page.send_form(constants.valid_bank_bin['bin'])
        assert constants.success_message in main_page.success_message.text

    def test_get_error_message_by_invalid_bin(self):
        main_page = MainPage2(self.driver)
        main_page.send_form(constants.invalid_ban_bin['bin'])
        assert constants.error_message in main_page.error_message.text
