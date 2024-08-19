import pytest
from flask import Flask

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    @app.route('/')
    def index():
        return 'Welcome to the Flask App'
    return app

def test_index(client) -> None:
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Flask App' in response.data
