
# 🧠 Purpose
# Encapsulate state-specific behavior in separate classes.

# Avoid complex conditional logic (if/else or switch).

# Promote Open/Closed Principle — add new states without modifying context.

# 🏪 Real-Life Analogy: Vending Machine
# A vending machine behaves differently depending on its state:

# NoCoinState

# HasCoinState

# DispensingState

# SoldOutState

# Each state handles user actions differently — e.g., you can't select a product without inserting a coin.

# ✅ Benefits
# Cleaner state-based logic (no nested if chains).

# Easy to add/remove states without touching existing logic.

# Better separation of concerns.




from abc import ABC, abstractmethod

# ----- State Interface -----
class VendingState(ABC):
    @abstractmethod
    def insert_coin(self, machine): pass

    @abstractmethod
    def select_product(self, machine, product): pass

    @abstractmethod
    def dispense(self, machine): pass


# ----- Concrete States -----
class NoCoinState(VendingState):
    def insert_coin(self, machine):
        print("[NoCoinState] Coin inserted.")
        machine.set_state(machine.has_coin_state)

    def select_product(self, machine, product):
        print("[NoCoinState] Insert coin first.")

    def dispense(self, machine):
        print("[NoCoinState] Insert coin first.")


class HasCoinState(VendingState):
    def insert_coin(self, machine):
        print("[HasCoinState] Coin already inserted.")

    def select_product(self, machine, product):
        if product not in machine.inventory or machine.inventory[product] <= 0:
            print(f"[HasCoinState] '{product}' is out of stock.")
            return
        print(f"[HasCoinState] '{product}' selected.")
        machine.selected_product = product
        machine.set_state(machine.dispensing_state)

    def dispense(self, machine):
        print("[HasCoinState] Select product first.")


class DispensingState(VendingState):
    def insert_coin(self, machine):
        print("[DispensingState] Please wait, dispensing in progress.")

    def select_product(self, machine, product):
        print("[DispensingState] Already selected. Please wait.")

    def dispense(self, machine):
        product = machine.selected_product
        if product:
            machine.inventory[product] -= 1
            print(f"[DispensingState] Dispensing '{product}'... Done!")
            machine.selected_product = None
            if all(v == 0 for v in machine.inventory.values()):
                machine.set_state(machine.sold_out_state)
            else:
                machine.set_state(machine.no_coin_state)


class SoldOutState(VendingState):
    def insert_coin(self, machine):
        print("[SoldOutState] Machine is sold out. Returning coin.")

    def select_product(self, machine, product):
        print("[SoldOutState] Machine is empty.")

    def dispense(self, machine):
        print("[SoldOutState] Nothing to dispense.")


# ----- Context: Vending Machine -----
class VendingMachine:
    def __init__(self, inventory):
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.dispensing_state = DispensingState()
        self.sold_out_state = SoldOutState()

        self.inventory = inventory
        self.selected_product = None

        self.state = self.no_coin_state if any(inventory.values()) else self.sold_out_state

    def set_state(self, state):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin(self)

    def select_product(self, product):
        self.state.select_product(self, product)

    def dispense(self):
        self.state.dispense(self)


# ----- Client Code -----
if __name__ == "__main__":
    inventory = {
        "Soda": 2,
        "Chips": 1
    }

    vm = VendingMachine(inventory)
    vm.select_product("Soda")      # No coin
    vm.insert_coin()
    vm.select_product("Soda")
    vm.dispense()                  # Dispense Soda

    vm.insert_coin()
    vm.select_product("Chips")
    vm.dispense()                  # Dispense Chips

    vm.insert_coin()              # Now sold out
