from selenium.webdriver.common.by import By


class MainPageLocators:
    INPUT_FIELD = (By.XPATH, '//input[@data-cy="input_bin"]')
    FORM_SEND_BUTTON = (By.XPATH, '//button[@data-cy="submit_button"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@class="alert alert-danger alert-dismissible fade show"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="alert alert-info alert-dismissible fade show"]')
    BIN_HEADER = (By.XPATH, '//th[@data-cy="bin"]')
    BIN_CELL = (By.XPATH, '//td[1]')

    BRAND_HEADER = (By.XPATH, '//th[@data-cy="brand"]')
    BRAND_CELL = (By.XPATH, '//td[2]')

    TYPE_HEADER = (By.XPATH, '//th[@data-cy="type"]')
    TYPE_CELL = (By.XPATH, '//td[3]')

    CATEGORY_HEADER = (By.XPATH, '//th[@data-cy="category"]')
    CATEGORY_CELL = (By.XPATH, '//td[4]')

    ISSUER_HEADER = (By.XPATH, '//th[@data-cy="issuer"]')
    ISSUER_CELL = (By.XPATH, '//td[5]')

    ALPHA_2_HEADER = (By.XPATH, '//th[@data-cy="alpha_2"]')
    ALPHA_2_CELL = (By.XPATH, '//td[6]')

    ALPHA_3_HEADER = (By.XPATH, '//th[@data-cy="alpha_3"]')
    ALPHA_3_CELL = (By.XPATH, '//td[7]')

    COUNTRY_HEADER = (By.XPATH, '//th[@data-cy="country"]')
    COUNTRY_CELL = (By.XPATH, '//td[8]')

    LATITUDE_HEADER = (By.XPATH, '//th[@data-cy="latitude"]')
    LATITUDE_CELL = (By.XPATH, '//td[9]')

    LONGITUDE_HEADER = (By.XPATH, '//th[@data-cy="longitude"]')
    LONGITUDE_CELL = (By.XPATH, '//td[10]')

    BANK_PHONE_HEADER = (By.XPATH, '//th[@data-cy="bank_phone"]')
    BANK_PHONE_CELL = (By.XPATH, '//td[11]')

    BANK_URL_HEADER = (By.XPATH, '//th[@data-cy="bank_url"]')
    BANK_URL_CELL = (By.XPATH, '//td[12]')
