# ✅ Purpose
# The Visitor Design Pattern lets you define new operations on a group of objects without changing their classes. It separates the algorithm from the object structure, which makes adding new operations easy, especially in systems with many object types.


# 🏪 Real-Life Analogy: Insurance Agent Visiting Different Assets
# Imagine an insurance agent (visitor) who visits various assets—like cars, houses, and electronics—to calculate insurance premiums. Instead of embedding premium logic in every asset class, we define a Visitor that encapsulates the premium rules.


from abc import ABC, abstractmethod

# ELEMENT INTERFACE
class Asset(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# CONCRETE ELEMENTS
class Car(Asset):
    def __init__(self, value, make):
        self.value = value
        self.make = make

    def accept(self, visitor):
        visitor.visit_car(self)

class House(Asset):
    def __init__(self, value, location):
        self.value = value
        self.location = location

    def accept(self, visitor):
        visitor.visit_house(self)

class Laptop(Asset):
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def accept(self, visitor):
        visitor.visit_laptop(self)

# VISITOR INTERFACE
class InsuranceAgent(ABC):
    @abstractmethod
    def visit_car(self, car):
        pass

    @abstractmethod
    def visit_house(self, house):
        pass

    @abstractmethod
    def visit_laptop(self, laptop):
        pass

# CONCRETE VISITOR
class PremiumCalculator(InsuranceAgent):
    def visit_car(self, car):
        premium = car.value * 0.05
        print(f"[Car] Make: {car.make} | Value: ₹{car.value} | Premium: ₹{premium}")

    def visit_house(self, house):
        premium = house.value * 0.02
        print(f"[House] Location: {house.location} | Value: ₹{house.value} | Premium: ₹{premium}")

    def visit_laptop(self, laptop):
        rate = 0.03 if laptop.brand == "Apple" else 0.02
        premium = laptop.cost * rate
        print(f"[Laptop] Brand: {laptop.brand} | Cost: ₹{laptop.cost} | Premium: ₹{premium}")

# CLIENT CODE
if __name__ == "__main__":
    assets = [
        Car(500000, "Hyundai"),
        House(2500000, "Mumbai"),
        Laptop("Apple", 120000),
        Laptop("Dell", 80000),
    ]

    visitor = PremiumCalculator()

    for asset in assets:
        asset.accept(visitor)




# 🛠️ Use Cases
# Use Case	Description
# Tax/Insurance systems	Apply different rules to assets, incomes, etc.
# Code analysis tools	Traverse AST (Abstract Syntax Tree)
# Shopping carts	Apply discounts based on item types
# Game entities	Different interactions for NPCs, obstacles, etc.

# 🎯 Why Use Visitor Pattern?
# When to Use	Why
# New operations on object structure	You avoid modifying all classes
# Objects have different types (polymorphic)	Centralizes logic outside the data structure
# You need type-specific behavior	visit_xxx() gives precise control