import unittest

from .common import get_test_client


class Test(unittest.TestCase):
    def test_route(self):
        r = get_test_client().get("/")
        assert r.status_code == 200
        assert r.json()["Hello"] == "World"
