import pytest


class TestGoogleSearch:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser  # Assign browser fixture to self.driver

    def test_search(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title