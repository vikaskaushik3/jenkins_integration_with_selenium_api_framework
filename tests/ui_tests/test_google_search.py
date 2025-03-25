import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("browser")
class TestGoogleSearch:
    def test_search(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Python")
        search_box.submit()
        assert "Google Search" in self.driver.title
