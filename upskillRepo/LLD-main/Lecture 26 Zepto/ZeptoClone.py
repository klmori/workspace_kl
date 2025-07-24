import math
from typing import List, Dict, Tuple

#############################################
# Product & Factory
#############################################

class Product:
    def __init__(self, sku: int, name: str, price: float):
        self.sku = sku
        self.name = name
        self.price = price

    def get_sku(self):
        return self.sku

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class ProductFactory:
    @staticmethod
    def create_product(sku: int) -> Product:
        if sku == 101:
            name, price = "Apple", 20
        elif sku == 102:
            name, price = "Banana", 10
        elif sku == 103:
            name, price = "Chocolate", 50
        elif sku == 201:
            name, price = "T-Shirt", 500
        elif sku == 202:
            name, price = "Jeans", 1000
        else:
            name, price = f"Item{sku}", 100
        return Product(sku, name, price)

#############################################
# InventoryStore (Interface) & DbInventoryStore
#############################################

class InventoryStore:
    def add_product(self, prod: Product, qty: int):
        raise NotImplementedError
    def remove_product(self, sku: int, qty: int):
        raise NotImplementedError
    def check_stock(self, sku: int) -> int:
        raise NotImplementedError
    def list_available_products(self) -> List[Product]:
        raise NotImplementedError

class DbInventoryStore(InventoryStore):
    def __init__(self):
        self.stock: Dict[int, int] = {}
        self.products: Dict[int, Product] = {}

    def add_product(self, prod: Product, qty: int):
        sku = prod.get_sku()
        if sku not in self.products:
            self.products[sku] = prod
        self.stock[sku] = self.stock.get(sku, 0) + qty

    def remove_product(self, sku: int, qty: int):
        if sku not in self.stock:
            return
        current_quantity = self.stock[sku]
        remaining_quantity = current_quantity - qty
        if remaining_quantity > 0:
            self.stock[sku] = remaining_quantity
        else:
            self.stock.pop(sku)
            self.products.pop(sku, None)

    def check_stock(self, sku: int) -> int:
        return self.stock.get(sku, 0)

    def list_available_products(self) -> List[Product]:
        return [self.products[sku] for sku, qty in self.stock.items() if qty > 0 and sku in self.products]

#############################################
# InventoryManager
#############################################

class InventoryManager:
    def __init__(self, store: InventoryStore):
        self.store = store

    def add_stock(self, sku: int, qty: int):
        prod = ProductFactory.create_product(sku)
        self.store.add_product(prod, qty)
        print(f"[InventoryManager] Added SKU {sku} Qty {qty}")

    def remove_stock(self, sku: int, qty: int):
        self.store.remove_product(sku, qty)

    def check_stock(self, sku: int) -> int:
        return self.store.check_stock(sku)

    def get_available_products(self) -> List[Product]:
        return self.store.list_available_products()

#############################################
# Replenishment Strategy (Strategy Pattern)
#############################################

class ReplenishStrategy:
    def replenish(self, manager: InventoryManager, items_to_replenish: Dict[int, int]):
        raise NotImplementedError

class ThresholdReplenishStrategy(ReplenishStrategy):
    def __init__(self, threshold: int):
        self.threshold = threshold

    def replenish(self, manager: InventoryManager, items_to_replenish: Dict[int, int]):
        print("[ThresholdReplenish] Checking threshold...")
        for sku, qty_to_add in items_to_replenish.items():
            current = manager.check_stock(sku)
            if current < self.threshold:
                manager.add_stock(sku, qty_to_add)
                print(f"  -> SKU {sku} was {current}, replenished by {qty_to_add}")

class WeeklyReplenishStrategy(ReplenishStrategy):
    def replenish(self, manager: InventoryManager, items_to_replenish: Dict[int, int]):
        print("[WeeklyReplenish] Weekly replenishment triggered for inventory.")

#############################################
# DarkStore
#############################################

class DarkStore:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y
        self.inventory_manager = InventoryManager(DbInventoryStore())
        self.replenish_strategy: ReplenishStrategy = None

    def distance_to(self, ux: float, uy: float) -> float:
        return math.sqrt((self.x - ux) ** 2 + (self.y - uy) ** 2)

    def run_replenishment(self, items_to_replenish: Dict[int, int]):
        if self.replenish_strategy:
            self.replenish_strategy.replenish(self.inventory_manager, items_to_replenish)

    def get_all_products(self) -> List[Product]:
        return self.inventory_manager.get_available_products()

    def check_stock(self, sku: int) -> int:
        return self.inventory_manager.check_stock(sku)

    def remove_stock(self, sku: int, qty: int):
        self.inventory_manager.remove_stock(sku, qty)

    def add_stock(self, sku: int, qty: int):
        self.inventory_manager.add_stock(sku, qty)

    def set_replenish_strategy(self, strategy: ReplenishStrategy):
        self.replenish_strategy = strategy

    def get_name(self):
        return self.name

    def get_x_coordinate(self):
        return self.x

    def get_y_coordinate(self):
        return self.y

    def get_inventory_manager(self):
        return self.inventory_manager

#############################################
# DarkStoreManager (Singleton)
#############################################

class DarkStoreManager:
    _instance = None

    def __init__(self):
        self.dark_stores: List[DarkStore] = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DarkStoreManager()
        return cls._instance

    def register_dark_store(self, ds: DarkStore):
        self.dark_stores.append(ds)

    def get_nearby_dark_stores(self, ux: float, uy: float, max_distance: float) -> List[DarkStore]:
        dist_list: List[Tuple[float, DarkStore]] = []
        for ds in self.dark_stores:
            d = ds.distance_to(ux, uy)
            if d <= max_distance:
                dist_list.append((d, ds))
        dist_list.sort(key=lambda x: x[0])
        return [ds for _, ds in dist_list]

#############################################
# User & Cart
#############################################

class Cart:
    def __init__(self):
        self.items: List[Tuple[Product, int]] = []

    def add_item(self, sku: int, qty: int):
        prod = ProductFactory.create_product(sku)
        self.items.append((prod, qty))
        print(f"[Cart] Added SKU {sku} ({prod.get_name()}) x{qty}")

    def get_total(self) -> float:
        return sum(prod.get_price() * qty for prod, qty in self.items)

    def get_items(self) -> List[Tuple[Product, int]]:
        return self.items

class User:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y
        self.cart = Cart()

    def get_cart(self) -> Cart:
        return self.cart

#############################################
# DeliveryPartner
#############################################

class DeliveryPartner:
    def __init__(self, name: str):
        self.name = name

#############################################
# Order & OrderManager (Singleton)
#############################################

class Order:
    next_id = 1
    def __init__(self, user: User):
        self.order_id = Order.next_id
        Order.next_id += 1
        self.user = user
        self.items: List[Tuple[Product, int]] = []
        self.partners: List[DeliveryPartner] = []
        self.total_amount = 0.0

class OrderManager:
    _instance = None

    def __init__(self):
        self.orders: List[Order] = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = OrderManager()
        return cls._instance

    def place_order(self, user: User, cart: Cart):
        print(f"\n[OrderManager] Placing Order for: {user.name}")
        requested_items = cart.get_items()
        max_dist = 5.0
        nearby_dark_stores = DarkStoreManager.get_instance().get_nearby_dark_stores(user.x, user.y, max_dist)
        if not nearby_dark_stores:
            print("  No dark stores within 5 KM. Cannot fulfill order.")
            return
        first_store = nearby_dark_stores[0]
        all_in_first = all(first_store.check_stock(prod.get_sku()) >= qty for prod, qty in requested_items)
        order = Order(user)
        if all_in_first:
            print(f"  All items at: {first_store.get_name()}")
            for prod, qty in requested_items:
                sku = prod.get_sku()
                first_store.remove_stock(sku, qty)
                order.items.append((prod, qty))
            order.total_amount = cart.get_total()
            order.partners.append(DeliveryPartner("Partner1"))
            print("  Assigned Delivery Partner: Partner1")
        else:
            print("  Splitting order across stores...")
            all_items = {prod.get_sku(): qty for prod, qty in requested_items}
            partner_id = 1
            for store in nearby_dark_stores:
                if not all_items:
                    break
                print(f"   Checking: {store.get_name()}")
                to_erase = []
                for sku, qty_needed in list(all_items.items()):
                    available_qty = store.check_stock(sku)
                    if available_qty <= 0:
                        continue
                    taken_qty = min(available_qty, qty_needed)
                    store.remove_stock(sku, taken_qty)
                    print(f"     {store.get_name()} supplies SKU {sku} x{taken_qty}")
                    order.items.append((ProductFactory.create_product(sku), taken_qty))
                    if qty_needed > taken_qty:
                        all_items[sku] = qty_needed - taken_qty
                    else:
                        to_erase.append(sku)
                for sku in to_erase:
                    all_items.pop(sku)
                if to_erase:
                    pname = f"Partner{partner_id}"
                    order.partners.append(DeliveryPartner(pname))
                    print(f"     Assigned: {pname} for {store.get_name()}")
            if all_items:
                print("  Could not fulfill:")
                for sku, qty in all_items.items():
                    print(f"    SKU {sku} x{qty}")
            order.total_amount = sum(prod.get_price() * qty for prod, qty in order.items)
        print(f"\n[OrderManager] Order #{order.order_id} Summary:")
        print(f"  User: {user.name}\n  Items:")
        for prod, qty in order.items:
            print(f"    SKU {prod.get_sku()} ({prod.get_name()}) x{qty} @ ₹{prod.get_price()}")
        print(f"  Total: ₹{order.total_amount}\n  Partners:")
        for dp in order.partners:
            print(f"    {dp.name}")
        print()
        self.orders.append(order)

    def get_all_orders(self) -> List[Order]:
        return self.orders

#############################################
# Zepto Initialization & Main
#############################################

class ZeptoHelper:
    @staticmethod
    def show_all_items(user: User):
        print(f"\n[Zepto] All Available products within 5 KM for {user.name}:")
        ds_manager = DarkStoreManager.get_instance()
        nearby_stores = ds_manager.get_nearby_dark_stores(user.x, user.y, 5.0)
        sku_to_price = {}
        sku_to_name = {}
        for ds in nearby_stores:
            for product in ds.get_all_products():
                sku = product.get_sku()
                if sku not in sku_to_price:
                    sku_to_price[sku] = product.get_price()
                    sku_to_name[sku] = product.get_name()
        for sku in sku_to_price:
            print(f"  SKU {sku} - {sku_to_name[sku]} @ ₹{sku_to_price[sku]}")

    @staticmethod
    def initialize():
        ds_manager = DarkStoreManager.get_instance()
        dark_store_a = DarkStore("DarkStoreA", 0.0, 0.0)
        dark_store_a.set_replenish_strategy(ThresholdReplenishStrategy(3))
        print("\nAdding stocks in DarkStoreA....")
        dark_store_a.add_stock(101, 5)
        dark_store_a.add_stock(102, 2)
        dark_store_b = DarkStore("DarkStoreB", 4.0, 1.0)
        dark_store_b.set_replenish_strategy(ThresholdReplenishStrategy(3))
        print("\nAdding stocks in DarkStoreB....")
        dark_store_b.add_stock(101, 3)
        dark_store_b.add_stock(103, 10)
        dark_store_c = DarkStore("DarkStoreC", 2.0, 3.0)
        dark_store_c.set_replenish_strategy(ThresholdReplenishStrategy(3))
        print("\nAdding stocks in DarkStoreC....")
        dark_store_c.add_stock(102, 5)
        dark_store_c.add_stock(201, 7)
        ds_manager.register_dark_store(dark_store_a)
        ds_manager.register_dark_store(dark_store_b)
        ds_manager.register_dark_store(dark_store_c)

if __name__ == "__main__":
    ZeptoHelper.initialize()
    user = User("Aditya", 1.0, 1.0)
    print(f"\nUser with name {user.name} comes on platform")
    ZeptoHelper.show_all_items(user)
    print("\nAdding items to cart")
    cart = user.get_cart()
    cart.add_item(101, 4)
    cart.add_item(102, 3)
    cart.add_item(103, 2)
    OrderManager.get_instance().place_order(user, cart)
    print("\n=== Demo Complete ===")
