# 🔍 Purpose
# The Proxy Pattern provides a placeholder or surrogate for another object to control access to it. It can be used for:

# Access control

# Lazy initialization

# Logging

# Security

# Rate limiting

# Remote proxies (e.g. RPC)



# 🧠 Real-Life Analogy: Credit Card as Proxy to Bank Account
# You don’t carry your entire bank account. Instead, you use a credit card (proxy) that:

# Validates your access

# Logs usage

# Prevents overspending

from abc import ABC, abstractmethod
import time
import random

# --------------------------------
# Subject Interface
# --------------------------------
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# --------------------------------
# Real Subject (expensive object)
# --------------------------------
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"[RealImage] Loading '{self.filename}' from disk...")
        time.sleep(1)  # Simulate expensive loading

    def display(self):
        print(f"[RealImage] Displaying image: {self.filename}")

# --------------------------------
# Proxy Object
# --------------------------------
class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
        self.load_count = 0

    def display(self):
        self.load_count += 1
        print(f"[Proxy] Request #{self.load_count} for '{self.filename}'")

        # Lazy loading
        if self.real_image is None:
            self.real_image = RealImage(self.filename)

        # Access control simulation
        if self.user_has_access():
            self.real_image.display()
        else:
            print("[Proxy] Access denied to image.")

    def user_has_access(self):
        # Simulate access control
        return random.choice([True, True, False])  # 66% access success

# --------------------------------
# Client Code
# --------------------------------
def client_code():
    print("=== Image Viewer Initialized ===")
    image1 = ImageProxy("car.jpg")
    image2 = ImageProxy("mountains.png")

    image1.display()  # Loads real image and displays
    print()
    image1.display()  # Uses already-loaded image
    print()
    image2.display()  # Loads new image
    print()
    image1.display()  # Again displays the same one

client_code()






# 🧰 Real-World Examples
# Domain	Example
# Web Browsers	Lazy-loading of images or videos
# Security Systems	Authentication proxy for secure resources
# Caching Systems	Redis/Memcached proxies
# ORM (like SQLAlchemy)	Lazy loading relationships
# API Gateway	Proxy between client and microservices
# Virtual Machines	Proxy object for memory-efficient management
# Payment Gateways	Payment proxy handling retries/authentication