import pytest
from selenium import webdriver
from django.conf import settings


@pytest.mark.usefixtures('driver')
class BasicSeleniumTest:
    pass


@pytest.fixture(params=["chrome", "firefox", "edge"], scope='class')
def driver(request):
    driver = None
    options = None
    if settings.USE_DOCKER:
        if request.param == "chrome":
            options = webdriver.ChromeOptions()
        if request.param == "firefox":
            options = webdriver.FirefoxOptions()
        if request.param == "edge":
            options = webdriver.EdgeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Remote(
            'http://selenium-hub:4444/wd/hub',
            options=options
        )
    else:
        if request.param == "chrome":
            driver = webdriver.Chrome()
        if request.param == "firefox":
            driver = webdriver.Firefox()
        if request.param == "edge":
            driver = webdriver.Edge()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()
