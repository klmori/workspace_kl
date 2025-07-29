# 🔍 Purpose
# The Builder Pattern is used to construct a complex object step by step. It separates the construction of an object from its representation, so the same construction process can create different representations.

# 🧠 Real-Life Analogy: Meal Order in a Restaurant
# When you order a meal:

# You choose different items (burger, drink, dessert) step-by-step.

# A waiter (builder) helps assemble it.

# The kitchen (director) controls the order and ensures it is made the right way.

# The meal (product) is the final result.

from abc import ABC, abstractmethod

# ----------------------------------------
# Product
# ----------------------------------------

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.os = None

    def show(self):
        print(f"Computer specs:")
        print(f"  CPU: {self.cpu}")
        print(f"  RAM: {self.ram}")
        print(f"  Storage: {self.storage}")
        print(f"  GPU: {self.gpu}")
        print(f"  OS: {self.os}")
        print()

# ----------------------------------------
# Builder Interface
# ----------------------------------------

class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()

    @abstractmethod
    def set_cpu(self): pass

    @abstractmethod
    def set_ram(self): pass

    @abstractmethod
    def set_storage(self): pass

    @abstractmethod
    def set_gpu(self): pass

    @abstractmethod
    def install_os(self): pass

    def get_computer(self):
        return self.computer

# ----------------------------------------
# Concrete Builders
# ----------------------------------------

class GamingComputerBuilder(ComputerBuilder):
    def set_cpu(self):
        self.computer.cpu = "Intel i9"

    def set_ram(self):
        self.computer.ram = "32GB DDR5"

    def set_storage(self):
        self.computer.storage = "2TB NVMe SSD"

    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"

    def install_os(self):
        self.computer.os = "Windows 11 Pro"

class OfficeComputerBuilder(ComputerBuilder):
    def set_cpu(self):
        self.computer.cpu = "Intel i5"

    def set_ram(self):
        self.computer.ram = "16GB DDR4"

    def set_storage(self):
        self.computer.storage = "512GB SSD"

    def set_gpu(self):
        self.computer.gpu = "Integrated Graphics"

    def install_os(self):
        self.computer.os = "Windows 10 Home"

# ----------------------------------------
# Director
# ----------------------------------------

class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self):
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_storage()
        self.builder.set_gpu()
        self.builder.install_os()
        return self.builder.get_computer()

# ----------------------------------------
# Client Code
# ----------------------------------------

def main():
    print("=== Gaming PC Build ===")
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    gaming_pc = director.build_computer()
    gaming_pc.show()

    print("=== Office PC Build ===")
    office_builder = OfficeComputerBuilder()
    director = ComputerDirector(office_builder)
    office_pc = director.build_computer()
    office_pc.show()

if __name__ == "__main__":
    main()


# 🛠 Real-World Use Cases
# Use Case	Builder Pattern Use
# HTML/XML Builders	Build tags step by step
# SQL Query Builders	Chainable methods to build query
# UI Form Builders	Dynamically generate UI elements
# Game Character Creation	Equip weapons, armor, skills
# Resume Builder Tool	Step-by-step generation of user profile