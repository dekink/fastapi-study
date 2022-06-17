import unittest

from .common import get_test_client


class Test(unittest.TestCase):
    def test_route(self):
        r = get_test_client().get("/")
        assert r.status_code == 200
        assert r.json()["Hello"] == "World"

    def test_create_user(self):
        # endpoint에 슬래쉬가 있었더니 307 temporary redirect
        # endpoitn마지막에 슬래쉬가 있을경우 redirect 함
        import time
        email = str(time.time())
        r = get_test_client().post(
            "/file/users",
            json={'email': email, 'password': 'ddd'}
        )
        assert r.status_code == 200
        result = r.json()

        r = get_test_client().get(
            f"/file/users/{result['id']}",
        )
        assert r.status_code == 200
        result = r.json()
        assert result['email'] == email
        assert result['is_active'] is True
