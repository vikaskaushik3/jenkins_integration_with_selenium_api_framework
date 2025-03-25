import requests

def test_github_api():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200
    assert "current_user_url" in response.json()
