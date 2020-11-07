from models.user import UserModel
from tests.unit.models.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel("test", "pass123")

        self.assertEqual("test", user.username, "The name of the user after creation does not equal the constructor "
                                                "argument.")
        self.assertEqual("pass123", user.password, "The password of the item after creation does not equal the "
                                                   "constructor argument.")
