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

import tempfile
import shutil
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def browser(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)  # Removed --user-data-dir

    yield driver
    driver.quit()
