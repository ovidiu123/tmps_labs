# SOLID Principles Report

## Single Responsibility Principle (SRP)
The `InventoryManager` class adheres to the Single Responsibility Principle by focusing solely on managing the inventory operations. It provides methods to:
- Add a product to the inventory (`add_product`).
- List all products (`list_products`).
- Retrieve all products (`get_products`).

This ensures that the inventory management logic is separated from other concerns like product creation or applying discounts.

### Code Example:
```python
class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(f"Name: {product.name}, Description: {product.description}, Price: ${product.price:.2f}")

    def get_products(self):
        return self.products

