from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# fixture for browser driver
@pytest.fixture(scope="class")
def browser(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
