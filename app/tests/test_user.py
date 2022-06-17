import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class Test(unittest.TestCase):
    def test_init(self):
        r = client.get("/")
        assert r.status_code == 200
        assert r.json()["Hello"] == "World"
