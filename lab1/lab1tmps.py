# Singleton Store Class
class Store:
    _instance = None

    def __init__(self):
        if Store._instance is not None:
            raise Exception("This class is a singleton!")
        self.inventory = []

    @staticmethod
    def get_instance():
        if Store._instance is None:
            Store._instance = Store()
        return Store._instance

    def add_product(self, product):
        self.inventory.append(product)

    def display_inventory(self):
        for product in self.inventory:
            product.display_product_info()


# Abstract Product Class
class Product:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_product_info(self):
        raise NotImplementedError("Subclasses should implement this method!")


# Computer Product
class Computer(Product):
    def __init__(self, brand, model, cpu, ram, storage):
        super().__init__(brand, model)
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def display_product_info(self):
        print(f"Computer - Brand: {self.brand}, Model: {self.model}, CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB")


# Smartphone Product
class Smartphone(Product):
    def __init__(self, brand, model, color, ram, storage):
        super().__init__(brand, model)
        self.color = color
        self.ram = ram
        self.storage = storage

    def display_product_info(self):
        print(f"Smartphone - Brand: {self.brand}, Model: {self.model}, Color: {self.color}, RAM: {self.ram}GB, Storage: {self.storage}GB")


# Abstract Factory Class
class ProductFactory:
    def create_product(self, brand, model):
        raise NotImplementedError("Subclasses should implement this method!")


# Computer Factory
class ComputerFactory(ProductFactory):
    def create_product(self, brand, model):
        return Computer(brand, model, "Intel i5", 8, 512)


# Smartphone Factory
class SmartphoneFactory(ProductFactory):
    def create_product(self, brand, model):
        return Smartphone(brand, model, "Black", 8, 128)


# Builder for Computer
class ComputerBuilder:
    def __init__(self):
        self.brand = None
        self.model = None
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_brand(self, brand):
        self.brand = brand
        return self

    def set_model(self, model):
        self.model = model
        return self

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.brand, self.model, self.cpu, self.ram, self.storage)


# Builder for Smartphone
class SmartphoneBuilder:
    def __init__(self):
        self.brand = None
        self.model = None
        self.color = None
        self.ram = None
        self.storage = None

    def set_brand(self, brand):
        self.brand = brand
        return self

    def set_model(self, model):
        self.model = model
        return self

    def set_color(self, color):
        self.color = color
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Smartphone(self.brand, self.model, self.color, self.ram, self.storage)


# Main Execution
if __name__ == "__main__":
    # Singleton Store Instance
    store = Store.get_instance()

    # Factory Method
    computer_factory = ComputerFactory()
    computer = computer_factory.create_product("Lenovo", "Legion 5i Pro")
    store.add_product(computer)

    smartphone_factory = SmartphoneFactory()
    smartphone = smartphone_factory.create_product("Samsung", "Galaxy S23")
    store.add_product(smartphone)

    # Builder for Custom Products
    custom_computer = (ComputerBuilder()
                       .set_brand("Asus")
                       .set_model("ROG")
                       .set_cpu("AMD Ryzen 7")
                       .set_ram(16)
                       .set_storage(512)
                       .build())
    store.add_product(custom_computer)

    custom_smartphone = (SmartphoneBuilder()
                         .set_brand("Apple")
                         .set_model("iPhone 16 Pro Max")
                         .set_color("Space Gray")
                         .set_ram(8)
                         .set_storage(512)
                         .build())
    store.add_product(custom_smartphone)

    # Display Inventory
    store.display_inventory()
