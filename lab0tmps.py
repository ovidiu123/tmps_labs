# Single Responsibility Principle: InventoryManager handles inventory operations
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


# Open/Closed Principle: Easily add new discount strategies without changing existing ones
class DiscountStrategy:
    def apply_discount(self, product):
        raise NotImplementedError("This method should be overridden by subclasses")


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, product):
        return product.price * (1 - self.percentage / 100)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, product):
        return max(product.price - self.amount, 0)  # Ensure price doesn't go below 0


# Adding a new discount strategy to demonstrate OCP
class BuyOneGetOneFree(DiscountStrategy):
    def apply_discount(self, product):
        # Example: Buy one, get one free logic (applied for demo purposes)
        return product.price / 2  # Assume one product is free for every pair


# Product and ProductFactory remain the same
class Product:

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class ProductFactory:
    @staticmethod
    def create_product(name, description, price):
        return Product(name, description, price)


# Main
if __name__ == "__main__":
    # Singleton: Only one inventory manager instance
    inventory_manager = InventoryManager()

    # Factory Method: Creating products via ProductFactory
    laptop = ProductFactory.create_product("Laptop", "High-end Laptop", 1500.0)
    smartphone = ProductFactory.create_product("Smartphone", "Latest Smartphone", 800.0)

    inventory_manager.add_product(laptop)
    inventory_manager.add_product(smartphone)

    print("Products before discounts:")
    inventory_manager.list_products()

    # Applying Percentage Discount Strategy
    percentage_discount = PercentageDiscount(20)
    for product in inventory_manager.get_products():
        discounted_price = percentage_discount.apply_discount(product)
        print(f"Discounted price for {product.name}: ${discounted_price:.2f}")

    # Applying Fixed Amount Discount Strategy
    fixed_discount = FixedAmountDiscount(100)
    for product in inventory_manager.get_products():
        discounted_price = fixed_discount.apply_discount(product)
        print(f"Discounted price for {product.name} with fixed discount: ${discounted_price:.2f}")

    # Applying Buy One Get One Free Strategy (newly added to demonstrate OCP)
    bogo_discount = BuyOneGetOneFree()
    for product in inventory_manager.get_products():
        discounted_price = bogo_discount.apply_discount(product)
        print(f"Discounted price for {product.name} with BOGO offer: ${discounted_price:.2f}")
