from tests.test_selenium.libs.locators.mainpage_locators import MainPageLocators
from tests.test_selenium.libs.pageobject.basepage import BasePage
from tests import constants


class MainPage1(BasePage):
    cells_map = {
        'bin': (MainPageLocators.BIN_HEADER, MainPageLocators.BIN_CELL),
        'brand': (MainPageLocators.BRAND_HEADER, MainPageLocators.BRAND_CELL),
        'type': (MainPageLocators.TYPE_HEADER, MainPageLocators.TYPE_CELL),
        'category': (MainPageLocators.CATEGORY_HEADER, MainPageLocators.CATEGORY_CELL),
        'issuer': (MainPageLocators.ISSUER_HEADER, MainPageLocators.ISSUER_CELL),
        'alpha_2': (MainPageLocators.ALPHA_2_HEADER, MainPageLocators.ALPHA_2_CELL),
        'alpha_3': (MainPageLocators.ALPHA_3_HEADER, MainPageLocators.ALPHA_3_CELL),
        'country': (MainPageLocators.COUNTRY_HEADER, MainPageLocators.COUNTRY_CELL),
        'latitude': (MainPageLocators.LATITUDE_HEADER, MainPageLocators.LATITUDE_CELL),
        'longitude': (MainPageLocators.LONGITUDE_HEADER, MainPageLocators.LONGITUDE_CELL),
        'bank_phone': (MainPageLocators.BANK_PHONE_HEADER, MainPageLocators.BANK_PHONE_CELL),
        'bank_url': (MainPageLocators.BANK_URL_HEADER, MainPageLocators.BANK_URL_CELL),
    }

    def enter_value(self, value):
        input_field = self.find_element(MainPageLocators.INPUT_FIELD)
        input_field.click()
        input_field.send_keys(value)

    def click_send_button(self):
        return self.find_element(MainPageLocators.FORM_SEND_BUTTON).click()

    def check_cell_value(self, field: str, value: str):
        self.find_element(self.cells_map[field][0])
        cell = self.find_element(self.cells_map[field][1])
        assert cell.text == value

    def check_all_cells_value(self, cells_value: str):
        for key, value in self.cells_map.items():
            self.find_element(value[0])
            cell = self.find_element(value[1])
            assert cell.text == cells_value[key]

    def check_success_message(self, success_message=constants.success_message):
        assert success_message in self.find_element(MainPageLocators.SUCCESS_MESSAGE).text

    def check_error_message(self, error_message=constants.error_message):
        assert error_message in self.find_element(MainPageLocators.ERROR_MESSAGE).text
