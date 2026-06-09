import pytest
import sys
import os

# Добавляем корень проекта в PYTHONPATH, чтобы можно было импортировать app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, Docker CI/CD!'