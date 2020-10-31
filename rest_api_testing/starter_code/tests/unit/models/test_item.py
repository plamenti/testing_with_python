from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def setUp(self) -> None:
        self.item = ItemModel("Test", 10.99)

    def test_create_item(self):
        self.assertEqual("Test", self.item.name, "Item name after creation is not correct!")
        self.assertEqual(10.99, self.item.price, "Item price after creation is not correct")

    def test_item_json(self):
        self.assertDictEqual({"name": "Test", "price": 10.99}, self.item.json(), "Item JSON after creation is not correct")
