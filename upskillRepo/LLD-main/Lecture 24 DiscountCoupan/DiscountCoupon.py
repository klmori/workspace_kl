import threading
from enum import Enum
from typing import List

# ----------------------------
# Discount Strategy (Strategy Pattern)
# ----------------------------
class DiscountStrategy:
    def calculate(self, base_amount: float) -> float:
        raise NotImplementedError

class FlatDiscountStrategy(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount
    def calculate(self, base_amount: float) -> float:
        return min(self.amount, base_amount)

class PercentageDiscountStrategy(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent
    def calculate(self, base_amount: float) -> float:
        return (self.percent / 100.0) * base_amount

class PercentageWithCapStrategy(DiscountStrategy):
    def __init__(self, percent: float, cap: float):
        self.percent = percent
        self.cap = cap
    def calculate(self, base_amount: float) -> float:
        disc = (self.percent / 100.0) * base_amount
        return min(disc, self.cap)

class StrategyType(Enum):
    FLAT = 1
    PERCENT = 2
    PERCENT_WITH_CAP = 3

# ----------------------------
# DiscountStrategyManager (Singleton)
# ----------------------------
class DiscountStrategyManager:
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        pass
    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = DiscountStrategyManager()
            return cls._instance
    def get_strategy(self, type_: StrategyType, param1: float, param2: float):
        if type_ == StrategyType.FLAT:
            return FlatDiscountStrategy(param1)
        elif type_ == StrategyType.PERCENT:
            return PercentageDiscountStrategy(param1)
        elif type_ == StrategyType.PERCENT_WITH_CAP:
            return PercentageWithCapStrategy(param1, param2)
        else:
            return None

# ----------------------------
# Product, CartItem, Cart
# ----------------------------
class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price
    def get_name(self):
        return self.name
    def get_category(self):
        return self.category
    def get_price(self):
        return self.price

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
    def item_total(self):
        return self.product.get_price() * self.quantity
    def get_product(self):
        return self.product

class Cart:
    def __init__(self):
        self.items: List[CartItem] = []
        self.original_total = 0.0
        self.current_total = 0.0
        self.loyalty_member = False
        self.payment_bank = ""
    def add_product(self, prod: Product, qty: int):
        item = CartItem(prod, qty)
        self.items.append(item)
        self.original_total += item.item_total()
        self.current_total += item.item_total()
    def get_original_total(self):
        return self.original_total
    def get_current_total(self):
        return self.current_total
    def apply_discount(self, d: float):
        self.current_total -= d
        if self.current_total < 0:
            self.current_total = 0
    def set_loyalty_member(self, member: bool):
        self.loyalty_member = member
    def is_loyalty_member(self):
        return self.loyalty_member
    def set_payment_bank(self, bank: str):
        self.payment_bank = bank
    def get_payment_bank(self):
        return self.payment_bank
    def get_items(self):
        return self.items

# ----------------------------
# Coupon base class (Chain of Responsibility)
# ----------------------------
class Coupon:
    def __init__(self):
        self.next = None
    def set_next(self, nxt):
        self.next = nxt
    def get_next(self):
        return self.next
    def apply_discount(self, cart: Cart):
        if self.is_applicable(cart):
            discount = self.get_discount(cart)
            cart.apply_discount(discount)
            print(f"{self.name()} applied: {discount}")
            if not self.is_combinable():
                return
        if self.next:
            self.next.apply_discount(cart)
    def is_applicable(self, cart: Cart):
        raise NotImplementedError
    def get_discount(self, cart: Cart):
        raise NotImplementedError
    def is_combinable(self):
        return True
    def name(self):
        raise NotImplementedError

# ----------------------------
# Concrete Coupons
# ----------------------------
class SeasonalOffer(Coupon):
    def __init__(self, percent: float, category: str):
        super().__init__()
        self.percent = percent
        self.category = category
        self.strat = DiscountStrategyManager.get_instance().get_strategy(StrategyType.PERCENT, percent, 0.0)
    def is_applicable(self, cart: Cart):
        return any(item.get_product().get_category() == self.category for item in cart.get_items())
    def get_discount(self, cart: Cart):
        subtotal = sum(item.item_total() for item in cart.get_items() if item.get_product().get_category() == self.category)
        return self.strat.calculate(subtotal)
    def name(self):
        return f"Seasonal Offer {int(self.percent)}% off {self.category}"

class LoyaltyDiscount(Coupon):
    def __init__(self, percent: float):
        super().__init__()
        self.percent = percent
        self.strat = DiscountStrategyManager.get_instance().get_strategy(StrategyType.PERCENT, percent, 0.0)
    def is_applicable(self, cart: Cart):
        return cart.is_loyalty_member()
    def get_discount(self, cart: Cart):
        return self.strat.calculate(cart.get_current_total())
    def name(self):
        return f"Loyalty Discount {int(self.percent)}% off"

class BulkPurchaseDiscount(Coupon):
    def __init__(self, threshold: float, flat_off: float):
        super().__init__()
        self.threshold = threshold
        self.flat_off = flat_off
        self.strat = DiscountStrategyManager.get_instance().get_strategy(StrategyType.FLAT, flat_off, 0.0)
    def is_applicable(self, cart: Cart):
        return cart.get_original_total() >= self.threshold
    def get_discount(self, cart: Cart):
        return self.strat.calculate(cart.get_current_total())
    def name(self):
        return f"Bulk Purchase Rs {int(self.flat_off)} off over {int(self.threshold)}"

class BankingCoupon(Coupon):
    def __init__(self, bank: str, min_spend: float, percent: float, off_cap: float):
        super().__init__()
        self.bank = bank
        self.min_spend = min_spend
        self.percent = percent
        self.off_cap = off_cap
        self.strat = DiscountStrategyManager.get_instance().get_strategy(StrategyType.PERCENT_WITH_CAP, percent, off_cap)
    def is_applicable(self, cart: Cart):
        return cart.get_payment_bank() == self.bank and cart.get_original_total() >= self.min_spend
    def get_discount(self, cart: Cart):
        return self.strat.calculate(cart.get_current_total())
    def name(self):
        return f"{self.bank} Bank Rs {int(self.percent)} off upto {int(self.off_cap)}"

# ----------------------------
# CouponManager (Singleton)
# ----------------------------
class CouponManager:
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        self.head = None
    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = CouponManager()
            return cls._instance
    def register_coupon(self, coupon: Coupon):
        with self._lock:
            if self.head is None:
                self.head = coupon
            else:
                cur = self.head
                while cur.get_next() is not None:
                    cur = cur.get_next()
                cur.set_next(coupon)
    def get_applicable(self, cart: Cart):
        with self._lock:
            res = []
            cur = self.head
            while cur:
                if cur.is_applicable(cart):
                    res.append(cur.name())
                cur = cur.get_next()
            return res
    def apply_all(self, cart: Cart):
        with self._lock:
            if self.head:
                self.head.apply_discount(cart)
            return cart.get_current_total()

# ----------------------------
# Main: Client code
# ----------------------------
if __name__ == "__main__":
    mgr = CouponManager.get_instance()
    mgr.register_coupon(SeasonalOffer(10, "Clothing"))
    mgr.register_coupon(LoyaltyDiscount(5))
    mgr.register_coupon(BulkPurchaseDiscount(1000, 100))
    mgr.register_coupon(BankingCoupon("ABC", 2000, 15, 500))

    p1 = Product("Winter Jacket", "Clothing", 1000)
    p2 = Product("Smartphone", "Electronics", 20000)
    p3 = Product("Jeans", "Clothing", 1000)
    p4 = Product("Headphones", "Electronics", 2000)

    cart = Cart()
    cart.add_product(p1, 1)
    cart.add_product(p2, 1)
    cart.add_product(p3, 2)
    cart.add_product(p4, 1)
    cart.set_loyalty_member(True)
    cart.set_payment_bank("ABC")

    print(f"Original Cart Total: {cart.get_original_total()} Rs")
    applicable = mgr.get_applicable(cart)
    print("Applicable Coupons:")
    for name in applicable:
        print(f" - {name}")
    final_total = mgr.apply_all(cart)
    print(f"Final Cart Total after discounts: {final_total} Rs")
