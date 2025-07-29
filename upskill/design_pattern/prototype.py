# ✅ Purpose
# The Prototype Design Pattern is used to create new objects by copying an existing object, known as the prototype. It helps in situations where object creation is costly or complex (e.g., database calls, network I/O, or heavy computations).

# 🏪 Real-Life Analogy: Cloning a Product Catalog
# Imagine an e-commerce platform like Zepto. When launching a new store, instead of re-entering all product details, they clone the catalog from another existing store and customize it.

# 🎯 Why Use Prototype?
# When object creation is expensive or slow

# When objects have many configuration options

# When you need to decouple object creation from usage



# 🛠️ Real-World Use Cases
# Domain	Example
# Game Dev	Cloning enemies or player units
# Design Software	Duplicate shapes with properties
# E-commerce	Clone product templates
# UI Systems	Reuse component trees (forms, templates)



import copy
from abc import ABC, abstractmethod

# Prototype Interface
class ProductPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete Prototype
class Product(ProductPrototype):
    def __init__(self, name, price, metadata=None):
        self.name = name
        self.price = price
        self.metadata = metadata or {}

    def clone(self):
        # Deep copy to ensure cloned object has its own copy of nested structures
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} | ₹{self.price} | Meta: {self.metadata}"

# Client that uses the prototype
class ProductCatalog:
    def __init__(self):
        self._products = {}

    def register_product(self, key, product):
        self._products[key] = product

    def get_product_clone(self, key):
        product = self._products.get(key)
        return product.clone() if product else None

# Client Code
if __name__ == "__main__":
    base_shampoo = Product("Anti-Dandruff Shampoo", 199, metadata={"brand": "Head & Shoulders", "volume": "180ml"})
    base_soap = Product("Luxury Soap", 99, metadata={"brand": "Dove", "scent": "Almond"})

    catalog = ProductCatalog()
    catalog.register_product("shampoo", base_shampoo)
    catalog.register_product("soap", base_soap)

    # Clone products for new city store
    new_shampoo = catalog.get_product_clone("shampoo")
    new_shampoo.metadata["brand"] = "Clinic Plus"  # Customize the clone

    new_soap = catalog.get_product_clone("soap")
    new_soap.price = 89  # Offer discount in new store

    print("Base Products:")
    print(base_shampoo)
    print(base_soap)

    print("\nCloned & Customized Products:")
    print(new_shampoo)
    print(new_soap)
