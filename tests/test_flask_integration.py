import requests

def test_flask_index_page():
    url = "http://localhost:8080"
    response = requests.get(url)
    
    assert response.status_code == 200, "Expected status code 200"
    assert "Welcome to the Flask App" in response.text, "Expected content not found"
