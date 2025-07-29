#  The Strategy Pattern allows selecting an algorithm or behavior at runtime.
# Instead of hardcoding logic, we define interchangeable strategies. 


 
# 🏪 Real-Life Analogy:
# Food Delivery App Checkout

# You want to pay for your food using different methods:

# Credit Card

# UPI

# Wallet

# Cash on Delivery

# Each has its own rules: validations, success rates, charges, etc.

# 🔧 With the Strategy Pattern, we can:

# Swap payment logic without touching the Checkout code.

# Add new payment types easily.

# Keep the code clean, maintainable, and extendable. 


from abc import ABC, abstractmethod
import random

# -----------------------
# Strategy Interface
# -----------------------
class PaymentStrategy(ABC):
    @abstractmethod
    def validate(self, amount):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

# -----------------------
# Concrete Strategies
# -----------------------
class CreditCardPayment(PaymentStrategy):
    def validate(self, amount):
        print("Validating Credit Card...")
        return amount <= 10000  # limit

    def pay(self, amount):
        print(f"Processing ₹{amount} via Credit Card")
        return random.choice([True, True, False])  # 66% success


class UPIPayment(PaymentStrategy):
    def validate(self, amount):
        print("Checking UPI app...")
        return True

    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI")
        return True  # always success


class WalletPayment(PaymentStrategy):
    def __init__(self, balance):
        self.balance = balance

    def validate(self, amount):
        print("Checking Wallet balance...")
        return self.balance >= amount

    def pay(self, amount):
        self.balance -= amount
        print(f"Paid ₹{amount} using Wallet. Remaining: ₹{self.balance}")
        return True

# -----------------------
# Context
# -----------------------
class CheckoutContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if not self.strategy.validate(amount):
            print("[Payment Failed] Validation error.")
            return False
        success = self.strategy.pay(amount)
        if success:
            print("[Payment Success]")
        else:
            print("[Payment Failed] Gateway error.")
        return success

# -----------------------
# Client Code
# -----------------------
if __name__ == "__main__":
    wallet = WalletPayment(balance=500)
    checkout = CheckoutContext(wallet)
    checkout.process_payment(300)

    checkout.set_strategy(UPIPayment())
    checkout.process_payment(800)

    checkout.set_strategy(CreditCardPayment())
    checkout.process_payment(12000)



# 💡 Benefits of Strategy Pattern
# ✅ Easy to extend — add new payment methods
# ✅ Open/Closed Principle — change behavior without modifying context
# ✅ Keeps code clean and testable
# ✅ Ideal for behavior that varies — sorting, routing, filtering, etc.