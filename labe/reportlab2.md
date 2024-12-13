# Structural Design Patterns in Python

**Author:** Ovidiu Lupan FAF-223

---

## 1. Introduction

This repository demonstrates the use of **Structural Design Patterns** in Python, which focus on simplifying the relationships among entities to build scalable and maintainable software. These patterns include:

1. **Adapter Pattern**: Enables incompatible interfaces to work together.
2. **Decorator Pattern**: Adds functionality dynamically to objects without altering their structure.
3. **Facade Pattern**: Provides a simplified interface to a complex subsystem.

### Key Benefits of Structural Patterns:
- Promotes code reusability.
- Ensures adherence to design principles like **Single Responsibility** and **Open-Closed Principle**.
- Enhances system modularity and scalability.

---

## 2. Patterns Implemented

### Adapter Pattern
The **Adapter Pattern** acts as a bridge between two incompatible interfaces. In this implementation, the `AdvancedProductAdapter` adapts the `Product` class to match the `AdvancedProduct` interface.

**Key Components:**
1. **`AdvancedProduct` Interface**: Defines the method `show_detailed_product_info()`.
2. **`AdvancedProductAdapter`**: Adapts `Product` to implement `AdvancedProduct`.

**Code Snippet:**
```python
# Adapter Example Usage
product = Product("Tablet", 400)
advanced_product = AdvancedProductAdapter(product)
advanced_product.show_detailed_product_info()
```

---

### Decorator Pattern
The **Decorator Pattern** dynamically adds behavior to objects without modifying their original structure. Here, the `DiscountDecorator` adds a discount feature to `Product` objects.

**Key Components:**
1. **`ProductDecorator`**: An abstract base class for decorators.
2. **`DiscountDecorator`**: Extends `ProductDecorator` to add a discount message.

**Code Snippet:**
```python
# Decorator Example Usage
basic_product = Product("Monitor", 300)
discounted_product = DiscountDecorator(basic_product, 10)
discounted_product.display_product_info()
```

---

### Facade Pattern
The **Facade Pattern** provides a unified interface to a set of interfaces in a subsystem. The `StoreFacade` simplifies interactions with the `Store` and `Product` classes.

**Key Components:**
1. **`Store`**: Manages a collection of products.
2. **`StoreFacade`**: Provides a simplified interface for managing inventory.

**Code Snippet:**
```python
# Facade Example Usage
facade = StoreFacade()
facade.add_product("Laptop", 1500)
facade.add_product("Smartphone", 800)
facade.show_inventory()
```

---

## 3. Running the Code

### Prerequisites:
Ensure you have Python 3 installed on your system.

### Steps:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd structural-patterns-python
   ```
3. Run the script:
   ```bash
   python structural_patterns.py
   ```

---

## 4. Conclusion

The implementation of structural design patterns in Python showcases their versatility in creating modular, extensible, and maintainable software systems. These patterns — **Adapter**, **Decorator**, and **Facade** — enhance functionality, simplify usage, and promote clean code architecture.

For further learning, refer to:
- [Refactoring Guru: Design Patterns](https://refactoring.guru/design-patterns)
- [Wikipedia: Structural Patterns](https://en.wikipedia.org/wiki/Structural_pattern)

