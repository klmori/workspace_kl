from abc import ABC, abstractmethod
from threading import Lock
from typing import List


# ----------------------------
# Strategy Pattern
# ----------------------------
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, base_amount: float) -> float:
        pass


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
        return min((self.percent / 100.0) * base_amount, self.cap)


class StrategyType:
    FLAT = "FLAT"
    PERCENT = "PERCENT"
    PERCENT_WITH_CAP = "PERCENT_WITH_CAP"


# ----------------------------
# Singleton: DiscountStrategyManager
# ----------------------------
class DiscountStrategyManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DiscountStrategyManager, cls).__new__(cls)
        return cls._instance

    def get_strategy(self, type_, param1, param2=0.0):
        if type_ == StrategyType.FLAT:
            return FlatDiscountStrategy(param1)
        elif type_ == StrategyType.PERCENT:
            return PercentageDiscountStrategy(param1)
        elif type_ == StrategyType.PERCENT_WITH_CAP:
            return PercentageWithCapStrategy(param1, param2)
        return None


# ----------------------------
# Product and Cart
# ----------------------------
class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price


class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def item_total(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []
        self.original_total = 0.0
        self.current_total = 0.0
        self.loyalty_member = False
        self.payment_bank = ""

    def add_product(self, product: Product, quantity: int):
        item = CartItem(product, quantity)
        self.items.append(item)
        self.original_total += item.item_total()
        self.current_total += item.item_total()

    def apply_discount(self, discount: float):
        self.current_total -= discount
        if self.current_total < 0:
            self.current_total = 0

    def set_loyalty_member(self, value: bool):
        self.loyalty_member = value

    def set_payment_bank(self, bank: str):
        self.payment_bank = bank


# ----------------------------
# Chain of Responsibility: Coupons
# ----------------------------
class Coupon(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, next_coupon):
        self._next = next_coupon

    def apply_discount(self, cart: Cart):
        if self.is_applicable(cart):
            discount = self.get_discount(cart)
            cart.apply_discount(discount)
            print(f"{self.name()} applied: {discount}")
            if not self.is_combinable():
                return
        if self._next:
            self._next.apply_discount(cart)

    @abstractmethod
    def is_applicable(self, cart: Cart) -> bool:
        pass

    @abstractmethod
    def get_discount(self, cart: Cart) -> float:
        pass

    def is_combinable(self) -> bool:
        return True

    @abstractmethod
    def name(self) -> str:
        pass


class SeasonalOffer(Coupon):
    def __init__(self, percent, category):
        super().__init__()
        self.percent = percent
        self.category = category
        self.strategy = DiscountStrategyManager().get_strategy(StrategyType.PERCENT, percent)

    def is_applicable(self, cart: Cart) -> bool:
        return any(item.product.category == self.category for item in cart.items)

    def get_discount(self, cart: Cart) -> float:
        subtotal = sum(item.item_total() for item in cart.items if item.product.category == self.category)
        return self.strategy.calculate(subtotal)

    def name(self):
        return f"Seasonal Offer {int(self.percent)}% off {self.category}"


class LoyaltyDiscount(Coupon):
    def __init__(self, percent):
        super().__init__()
        self.percent = percent
        self.strategy = DiscountStrategyManager().get_strategy(StrategyType.PERCENT, percent)

    def is_applicable(self, cart: Cart) -> bool:
        return cart.loyalty_member

    def get_discount(self, cart: Cart) -> float:
        return self.strategy.calculate(cart.current_total)

    def name(self):
        return f"Loyalty Discount {int(self.percent)}% off"


class BulkPurchaseDiscount(Coupon):
    def __init__(self, threshold, flat_off):
        super().__init__()
        self.threshold = threshold
        self.flat_off = flat_off
        self.strategy = DiscountStrategyManager().get_strategy(StrategyType.FLAT, flat_off)

    def is_applicable(self, cart: Cart) -> bool:
        return cart.original_total >= self.threshold

    def get_discount(self, cart: Cart) -> float:
        return self.strategy.calculate(cart.current_total)

    def name(self):
        return f"Bulk Purchase Rs {int(self.flat_off)} off over {int(self.threshold)}"


class BankingCoupon(Coupon):
    def __init__(self, bank, min_spend, percent, cap):
        super().__init__()
        self.bank = bank
        self.min_spend = min_spend
        self.percent = percent
        self.cap = cap
        self.strategy = DiscountStrategyManager().get_strategy(StrategyType.PERCENT_WITH_CAP, percent, cap)

    def is_applicable(self, cart: Cart) -> bool:
        return cart.payment_bank == self.bank and cart.original_total >= self.min_spend

    def get_discount(self, cart: Cart) -> float:
        return self.strategy.calculate(cart.current_total)

    def name(self):
        return f"{self.bank} Bank Rs {int(self.percent)} off upto {int(self.cap)}"


# ----------------------------
# Singleton: CouponManager
# ----------------------------
class CouponManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CouponManager, cls).__new__(cls)
            cls._instance._head = None
            cls._instance._lock = Lock()
        return cls._instance

    def register_coupon(self, coupon: Coupon):
        with self._lock:
            if self._head is None:
                self._head = coupon
            else:
                current = self._head
                while current._next:
                    current = current._next
                current.set_next(coupon)

    def get_applicable(self, cart: Cart) -> List[str]:
        with self._lock:
            res = []
            current = self._head
            while current:
                if current.is_applicable(cart):
                    res.append(current.name())
                current = current._next
            return res

    def apply_all(self, cart: Cart) -> float:
        with self._lock:
            if self._head:
                self._head.apply_discount(cart)
            return cart.current_total


# ----------------------------
# Main (Client Code)
# ----------------------------
if __name__ == "__main__":
    mgr = CouponManager()
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

    print("Original Cart Total:", cart.original_total, "Rs")
    applicable = mgr.get_applicable(cart)
    print("Applicable Coupons:")
    for name in applicable:
        print(" -", name)

    final_total = mgr.apply_all(cart)
    print("Final Cart Total after discounts:", final_total, "Rs")
