from __future__ import annotations

from typing import List

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        self.purchase_history.append(transaction)

class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity: int):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity

class ItemCollection:
    def __init__(self):
        self.items: List[FoodItem] = []

    def add_item(self, item: FoodItem):
        self.items.append(item)

    def filter_by_category(self, category: str) -> List[FoodItem]:
        return [item for item in self.items if item.category == category]

class Transaction:
    def __init__(self, items: List[FoodItem]):
        self.items = items
        self.total = self.calculate_total()

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)