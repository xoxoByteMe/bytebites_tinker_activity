# test_bytebites.py

import unittest
from models import Customer, FoodItem, ItemCollection, Transaction

class TestByteBites(unittest.TestCase):

    def test_order_totals(self):
        """Test that Transaction calculates the total cost correctly for multiple items."""
        item1 = FoodItem("Burger", 5.0, "Main", 10)
        item2 = FoodItem("Fries", 2.0, "Side", 8)
        transaction = Transaction([item1, item2])
        self.assertEqual(transaction.calculate_total(), 7.0)

    def test_empty_totals(self):
        """Test that Transaction returns 0 for an empty list of items."""
        transaction = Transaction([])
        self.assertEqual(transaction.calculate_total(), 0.0)

    def test_filter_by_category(self):
        """Test that ItemCollection filters items by category correctly."""
        collection = ItemCollection()
        item1 = FoodItem("Burger", 5.0, "Main", 10)
        item2 = FoodItem("Fries", 2.0, "Side", 8)
        item3 = FoodItem("Soda", 1.5, "Drink", 5)
        collection.add_item(item1)
        collection.add_item(item2)
        collection.add_item(item3)
        filtered = collection.filter_by_category("Main")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].name, "Burger")

if __name__ == '__main__':
    unittest.main()