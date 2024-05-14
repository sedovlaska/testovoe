import pytest
from selenium import webdriver
from django.conf import settings


@pytest.mark.usefixtures('driver')
class BasicSeleniumTest:
    pass


@pytest.fixture(scope='class')
def driver(request):
    if settings.USE_DOCKER:
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option('prefs', {
            "download.prompt_for_download": True,
            "plugins.always_open_pdf_externally": False
        })
        driver = webdriver.Remote(
            'http://chrome:4444/wd/hub',
            options=options
        )
    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()
