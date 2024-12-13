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
