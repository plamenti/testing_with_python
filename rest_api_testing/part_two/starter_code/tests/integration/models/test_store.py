from models.item import ItemModel
from models.store import StoreModel
from tests.integration.integration_base_test import IntegrationBaseTest


class StoreTest(IntegrationBaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel("test")

        self.assertListEqual([], store.items.all(), "The store's items length should be 0 after creating store")

    def test_crud(self):
        with self.app_context():
            store = StoreModel("test")

            self.assertIsNone(StoreModel.find_by_name("test"))

            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name("test"))

            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name("test"))

    def test_store_relationships(self):
        with self.app_context():
            store = StoreModel("test")
            item = ItemModel("test_item", 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(1, store.items.count())
            self.assertEqual("test_item", store.items.first().name)

    def test_store_json(self):
        store = StoreModel("test")
        expected_json = {
            "name": "test",
            "items": []
        }

        self.assertDictEqual(expected_json, store.json())

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel("test")
            item = ItemModel("test_item", 19.99, 1)

            store.save_to_db()
            item.save_to_db()
            
            expected_json = {
                "name": "test",
                "items": [{"name": "test_item", "price": 19.99}]
            }

            self.assertDictEqual(expected_json, store.json())
