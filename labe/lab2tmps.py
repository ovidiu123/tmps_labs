from abc import ABC, abstractmethod

# --- Adapter Pattern ---

# Domain Classes
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product_info(self):
        print(f"Product Name: {self.name}, Price: ${self.price}")

# AdvancedProduct Interface
class AdvancedProduct(ABC):
    @abstractmethod
    def show_detailed_product_info(self):
        pass

# Adapter
class AdvancedProductAdapter(AdvancedProduct):
    def __init__(self, product):
        self.product = product

    def show_detailed_product_info(self):
        self.product.display_product_info()
        print("Additional info: This product is available in limited stock.")

# --- Decorator Pattern ---

# Base Decorator
class ProductDecorator(Product):
    def __init__(self, decorated_product):
        self.decorated_product = decorated_product

    def display_product_info(self):
        self.decorated_product.display_product_info()

# Concrete Decorator
class DiscountDecorator(ProductDecorator):
    def __init__(self, decorated_product, discount_percentage):
        super().__init__(decorated_product)
        self.discount_percentage = discount_percentage

    def display_product_info(self):
        super().display_product_info()
        print(f"Discount: {self.discount_percentage}% off")

# --- Facade Pattern ---

# Store class
class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_inventory(self):
        for product in self.products:
            product.display_product_info()

# StoreFacade
class StoreFacade:
    def __init__(self):
        self.store = Store()

    def add_product(self, name, price):
        product = Product(name, price)
        self.store.add_product(product)

    def show_inventory(self):
        self.store.display_inventory()

# --- Example Usage ---
if __name__ == "__main__":
    # Facade Example
    facade = StoreFacade()
    facade.add_product("Laptop", 1500)
    facade.add_product("Smartphone", 800)
    print("Store Inventory:")
    facade.show_inventory()

    # Adapter Example
    print("\nUsing Adapter Pattern:")
    product = Product("Tablet", 400)
    advanced_product = AdvancedProductAdapter(product)
    advanced_product.show_detailed_product_info()

    # Decorator Example
    print("\nUsing Decorator Pattern:")
    basic_product = Product("Monitor", 300)
    discounted_product = DiscountDecorator(basic_product, 10)
    discounted_product.display_product_info()
