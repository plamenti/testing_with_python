import json

from app.tests.system.base_test import BaseTest


class TestHome(BaseTest):
    def test_home(self):
        with self.app as c:
            resp = c.get("/")

            self.assertEqual(resp.status_code, 200)
            self.assertDictEqual({"message": "Hello, world!"}, json.loads(resp.get_data()))
