# Structural Design Patterns in Python

**Author:** Lupan Ovidiu, FAF-223

---

## Introduction

This repository demonstrates the use of **Structural Design Patterns** in Python. These patterns simplify the relationships among entities, making software more scalable, maintainable, and modular.

### Patterns Implemented:
1. **Adapter Pattern**: Enables incompatible interfaces to work together.
2. **Decorator Pattern**: Dynamically adds functionality to objects.
3. **Facade Pattern**: Provides a simplified interface to a complex subsystem.

### Key Benefits:
- Promotes **code reusability**.
- Adheres to principles like **Single Responsibility** and **Open-Closed Principle**.
- Enhances modularity and scalability.

---

## Patterns Explained

### Adapter Pattern
The **Adapter Pattern** bridges two incompatible interfaces. In this implementation, the `AdvancedProductAdapter` adapts the `Product` class to match the `AdvancedProduct` interface.

**Key Components:**
- **`AdvancedProduct` Interface**: Declares the `show_detailed_product_info()` method.
- **`AdvancedProductAdapter`**: Adapts `Product` to implement `AdvancedProduct`.

**Example Usage:**
```python
product = Product("Tablet", 400)
advanced_product = AdvancedProductAdapter(product)
advanced_product.show_detailed_product_info()
Decorator Pattern
The Decorator Pattern dynamically extends the functionality of objects without modifying their base class.

Key Components:

ProductDecorator: Base decorator class.
DiscountDecorator: Adds discount information to the Product.
Example Usage:

python
Copiază codul
basic_product = Product("Monitor", 300)
discounted_product = DiscountDecorator(basic_product, 10)
discounted_product.display_product_info()
Facade Pattern
The Facade Pattern simplifies interactions with a complex system. Here, the StoreFacade consolidates inventory management into a single interface.

Key Components:

Store: Manages inventory.
StoreFacade: Provides a user-friendly interface to Store.
Example Usage:

python
Copiază codul
facade = StoreFacade()
facade.add_product("Laptop", 1500)
facade.add_product("Smartphone", 800)
facade.show_inventory()
Code
The entire implementation is contained in the file structural_patterns.py. Below is the full code:

python
Copiază codul
# structural_patterns.py

# Product Class
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def display_product_info(self):
        print(f"Product Name: {self.name}, Price: ${self.price}")


# Adapter Pattern Implementation
class AdvancedProduct:
    def show_detailed_product_info(self):
        raise NotImplementedError("This method should be overridden.")

class AdvancedProductAdapter(AdvancedProduct):
    def __init__(self, product: Product):
        self.product = product

    def show_detailed_product_info(self):
        print(f"Product Name: {self.product.name}, Price: ${self.product.price}")
        print("Additional info: This product is available in limited stock.")


# Decorator Pattern Implementation
class ProductDecorator:
    def __init__(self, product: Product):
        self.product = product

    def display_product_info(self):
        self.product.display_product_info()

class DiscountDecorator(ProductDecorator):
    def __init__(self, product: Product, discount_percentage: float):
        super().__init__(product)
        self.discount_percentage = discount_percentage

    def display_product_info(self):
        super().display_product_info()
        print(f"Discount: {self.discount_percentage}% off")


# Facade Pattern Implementation
class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, name: str, price: float):
        product = Product(name, price)
        self.inventory.append(product)

    def show_inventory(self):
        if not self.inventory:
            print("No products in inventory.")
        else:
            print("Store Inventory:")
            for product in self.inventory:
                product.display_product_info()

class StoreFacade:
    def __init__(self):
        self.store = Store()

    def add_product(self, name: str, price: float):
        self.store.add_product(name, price)

    def show_inventory(self):
        self.store.show_inventory()


# Main Function
def main():
    print("### Adapter Pattern ###")
    product = Product("Tablet", 400)
    advanced_product = AdvancedProductAdapter(product)
    advanced_product.show_detailed_product_info()

    print("\n### Decorator Pattern ###")
    basic_product = Product("Monitor", 300)
    discounted_product = DiscountDecorator(basic_product, 10)
    discounted_product.display_product_info()

    print("\n### Facade Pattern ###")
    facade = StoreFacade()
    facade.add_product("Laptop", 1500)
    facade.add_product("Smartphone", 800)
    facade.show_inventory()


if __name__ == "__main__":
    main()
How to Run
Clone the repository:
bash
Copiază codul
git clone <repository-url>
Navigate to the project directory:
bash
Copiază codul
cd structural-patterns-python
Run the script:
bash
Copiază codul
python structural_patterns.py
Sample Output
yaml
Copiază codul
### Adapter Pattern ###
Product Name: Tablet, Price: $400
Additional info: This product is available in limited stock.

### Decorator Pattern ###
Product Name: Monitor, Price: $300
Discount: 10% off

### Facade Pattern ###
Store Inventory:
Product Name: Laptop, Price: $1500
Product Name: Smartphone, Price: $800
Conclusion
The implementation of the Adapter, Decorator, and Facade patterns showcases their utility in creating modular and maintainable software. These patterns make it easier to adapt, extend, and simplify functionality while adhering to clean code principles.

