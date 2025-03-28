import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def browser(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--headless")  # Optional: Uncomment if running in CI/CD
    options.add_argument("--disable-gpu")  # Avoids GPU-related issues
    options.add_argument("--no-sandbox")  # Required for running in Docker/Linux
    options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues in containers

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        pytest.fail(f"Failed to start WebDriver: {str(e)}")

    yield driver
    driver.quit()
