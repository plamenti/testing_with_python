from tests.base_test import BaseTest
from models.item import ItemModel

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel("Test", 10.99)

            self.assertIsNone(ItemModel.find_by_name("Test"))
            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name("Test"))
            
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name("Test"))