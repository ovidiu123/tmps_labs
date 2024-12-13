# **Tech Store Application: Design Patterns Implementation**

## **Introduction**
This project demonstrates the use of multiple design patterns in a tech store application. It features a system for managing an inventory of products such as computers and smartphones, emphasizing modularity, reusability, and scalability in the design.

The following design patterns are implemented:
1. **Singleton Pattern**: Ensures a single instance of the `Store` class to manage the product inventory.
2. **Factory Method Pattern**: Simplifies the creation of different product types (e.g., `Computer` and `Smartphone`) through dedicated factories.
3. **Builder Pattern**: Facilitates the step-by-step creation of complex product objects with numerous customizable attributes.

---

## **Design Patterns Used**

### **1. Singleton Pattern**
- **Purpose**: Ensures that only one instance of the `Store` class exists throughout the application, maintaining a centralized inventory.
- **Implementation**:
  - The `Store` class has a private static instance and a private constructor to restrict external instantiation.
  - A public static method `getInstance` ensures access to the single instance of the class.
- **Advantages**:
  - Ensures consistent management of the store inventory.
  - Provides a global point of access to the `Store` object.
- **Example Code**:
  ```java
  Store store = Store.getInstance();

2. Factory Method Pattern
Purpose: Provides an interface for creating objects in a superclass but allows subclasses to decide which object to instantiate.
Implementation:
The ProductFactory abstract class defines the structure for creating products.
Concrete factories (ComputerFactory, SmartphoneFactory) implement ProductFactory to create specific products.
Advantages:
Decouples the product creation process from client code.
Makes adding new product types easier without modifying existing code.

3. Builder Pattern
Purpose: Simplifies the creation of complex objects by constructing them step-by-step with optional parameters.
Implementation:
Builders (ComputerBuilder, SmartphoneBuilder) provide methods for setting individual attributes of a product.
The build method finalizes the creation and returns the customized product object.
Advantages:
Provides clarity in creating products with multiple optional attributes.
Facilitates the reuse of code for different product configurations.
Conclusion
This implementation showcases the effectiveness of design patterns in creating a scalable, modular, and easily extendable application. By using the Singleton, Factory Method, and Builder patterns, the project achieves clean code, better maintainability, and flexibility for future enhancements.
