from models.store import StoreModel
from tests.unit.models.unit_base_test import UnitBaseTest


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel("test")

        self.assertEqual("test", store.name,
                         "The name of the store after creation is not equal the constructor argument")
