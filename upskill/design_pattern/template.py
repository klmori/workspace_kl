# 🔍 Purpose
# The Template Method Pattern defines the skeleton of an algorithm in a base class but lets subclasses override specific steps without changing the algorithm’s structure.


# 🧠 Real-Life Analogy: Online Ordering System (like Zepto or Swiggy)
# Consider an online order system:

# Steps like selectItems, makePayment, generateInvoice, deliverItems are common.

# But the way items are selected or delivered may vary for GroceryOrder, RestaurantOrder, etc.



from abc import ABC, abstractmethod

# ------------------------------
# Template Base Class
# ------------------------------
class OrderProcessor(ABC):
    # Template Method (final algorithm)
    def process_order(self):
        self.select_items()
        self.make_payment()
        self.generate_invoice()
        self.deliver_items()
        self.send_notification()

    @abstractmethod
    def select_items(self):
        pass

    @abstractmethod
    def make_payment(self):
        pass

    def generate_invoice(self):
        print("[Invoice] Generating standard invoice...")

    @abstractmethod
    def deliver_items(self):
        pass

    # Hook method (can be optionally overridden)
    def send_notification(self):
        print("[Notification] Sending order confirmation...")

# ------------------------------
# Concrete Class: Grocery Order
# ------------------------------
class GroceryOrder(OrderProcessor):
    def select_items(self):
        print("[Grocery] Selecting vegetables, fruits and snacks...")

    def make_payment(self):
        print("[Grocery] Payment made via UPI...")

    def deliver_items(self):
        print("[Grocery] Delivered via delivery van within 1 hour.")

# ------------------------------
# Concrete Class: Restaurant Order
# ------------------------------
class RestaurantOrder(OrderProcessor):
    def select_items(self):
        print("[Restaurant] Selecting food items from menu...")

    def make_payment(self):
        print("[Restaurant] Payment made via credit card...")

    def deliver_items(self):
        print("[Restaurant] Food delivered by delivery partner in 30 mins.")

    def send_notification(self):
        print("[Restaurant] SMS and email sent to customer.")

# ------------------------------
# Client Code
# ------------------------------
def client_code():
    print("---- Grocery Order ----")
    grocery = GroceryOrder()
    grocery.process_order()

    print("\n---- Restaurant Order ----")
    food = RestaurantOrder()
    food.process_order()

client_code()









# 📦 Where It’s Used
# Domain	Example
# Order Processing	Different vendors have same order flow
# UI Frameworks	Lifecycle hooks (onLoad, onDraw, etc.)
# Games	Game loop with update(), draw()
# Compiler	Tokenizing → Parsing → Code generation
# Frameworks (like Django)	Middleware, Request/Response lifecycle