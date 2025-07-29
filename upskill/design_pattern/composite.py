# ✅ Purpose

# 🧠 Real-life analogy

# 💻 Complex Python code example

# ⏱ Time complexity

# ✅ Where it's used in real systems



# 🧠 Real-Life Analogy
# Imagine you're building a Zepto-like app with a cart system:

# Leaf: A single product (e.g., Apple, Milk)

# Composite: A bundle or category (e.g., "Fruits", "Grocery", "Weekly Combo Pack")

# You want to perform operations like:

# Get total price of a bundle (recursively add all prices)

# Print product/category list

# Apply discounts on bundles or items



from abc import ABC, abstractmethod

# -----------------------------------
# Component Base Class
# -----------------------------------
class CartComponent(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def display(self, indent=0):
        pass


# -----------------------------------
# Leaf Class - A Single Product
# -----------------------------------
class Product(CartComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def display(self, indent=0):
        print(" " * indent + f"- Product: {self.name} (₹{self.price})")


# -----------------------------------
# Composite Class - Can contain multiple products or groups
# -----------------------------------
class ProductBundle(CartComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component: CartComponent):
        self.items.append(component)

    def remove(self, component: CartComponent):
        self.items.remove(component)

    def get_price(self):
        return sum(item.get_price() for item in self.items)

    def display(self, indent=0):
        print(" " * indent + f"+ Bundle: {self.name}")
        for item in self.items:
            item.display(indent + 2)


# -----------------------------------
# Client code simulating a cart
# -----------------------------------
if __name__ == "__main__":
    # Create individual products
    apple = Product("Apple", 40)
    banana = Product("Banana", 30)
    milk = Product("Milk", 50)
    bread = Product("Bread", 25)
    cheese = Product("Cheese", 60)

    # Create bundle: Fruits
    fruits_bundle = ProductBundle("Fruits")
    fruits_bundle.add(apple)
    fruits_bundle.add(banana)

    # Create bundle: Dairy
    dairy_bundle = ProductBundle("Dairy")
    dairy_bundle.add(milk)
    dairy_bundle.add(cheese)

    # Create Main Weekly Combo
    weekly_combo = ProductBundle("Weekly Combo")
    weekly_combo.add(fruits_bundle)
    weekly_combo.add(dairy_bundle)
    weekly_combo.add(bread)

    # Display Cart Tree
    weekly_combo.display()

    # Total Price
    print("\nTotal Cart Price: ₹", weekly_combo.get_price())




# 🧩 Real-World Uses of Composite Pattern
# Domain	Use Case Example
# UI Frameworks	Buttons inside Panels, inside Windows (e.g. HTML DOM)
# File Systems	File and Folder hierarchy (File, Directory)
# Product Bundles (ecom)	Bundles within bundles in shopping cart
# Graphic Editors	Shapes grouped into diagrams
# Task Scheduling Systems	Parent task with subtasks