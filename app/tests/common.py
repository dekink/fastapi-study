from app.main import app

from fastapi.testclient import TestClient


def get_test_client():
    return TestClient(app)