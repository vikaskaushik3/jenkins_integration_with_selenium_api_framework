# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import pytest
#
# # fixture for browser driver
# @pytest.fixture(scope="class")
# def browser(request):
#     options = webdriver.ChromeOptions()
#     options.binary_location = "/usr/bin/google-chrome"
#
#     # Use a temporary directory for user data
#     import tempfile
#     user_data_dir = tempfile.mkdtemp()
#     options.add_argument(f"--user-data-dir={user_data_dir}")
#
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def browser(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()
