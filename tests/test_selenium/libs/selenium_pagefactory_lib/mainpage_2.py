from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from tests.constants import base_url


class MainPage2(PageFactory):
    locators = {
        'input_field': (By.XPATH, '//input[@data-cy="input_bin"]'),
        'submit_button': (By.XPATH, '//button[@data-cy="submit_button"]'),
        'error_message': (By.XPATH, '//div[@class="alert alert-danger alert-dismissible fade show"]'),
        'success_message': (By.XPATH, '//div[@class="alert alert-info alert-dismissible fade show"]'),
    }

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.base_url = base_url
        self.driver.get(self.base_url)

    def send_form(self, value):
        self.input_field.set_text(value)
        self.submit_button.click()
