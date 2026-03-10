# Draft UML Class Diagram for ByteBites App

Below is the UML class diagram in Mermaid syntax, based on the ByteBites specification.

```mermaid
classDiagram
    class Customer {
        +str name
        +list~Transaction~ purchase_history
        +__init__(name: str)
        +add_transaction(transaction: Transaction)
    }

    class FoodItem {
        +str name
        +float price
        +str category
        +int popularity
        +__init__(name: str, price: float, category: str, popularity: int)
    }

    class ItemCollection {
        +list~FoodItem~ items
        +__init__()
        +add_item(item: FoodItem)
        +filter_by_category(category: str): list~FoodItem~
    }

    class Transaction {
        +list~FoodItem~ items
        +float total
        +__init__(items: list~FoodItem~)
        +calculate_total(): float
    }

    Customer ||--o{ Transaction : has
    ItemCollection ||--o{ FoodItem : contains
    Transaction ||--o{ FoodItem : includes