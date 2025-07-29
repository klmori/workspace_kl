# 🔍 Purpose
# The Singleton Pattern ensures that only one instance of a class is created and used globally. It is often used for shared resources like:

# Database connections

# Configuration managers

# Logging systems

# Caching mechanisms

# Payment service gateways




# 🏪 Real-Life Analogy
# Imagine you're running a Zepto-like food delivery app. You need only one instance of a:

# Payment Gateway Manager – to coordinate payments

# Logging System – to log all transactions globally

# App Configuration Loader – to read configs only once and reuse

# Creating multiple instances wastes resources and can break global coordination. Singleton solves this.


import threading

# -----------------------------------------
# Singleton Logger (used across the system)
# -----------------------------------------
class Logger:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("Use Logger.get_instance() to access the singleton!")
        self.logs = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = Logger()
        return cls._instance

    def log(self, message):
        self.logs.append(message)
        print(f"[LOG]: {message}")

    def show_all_logs(self):
        print("\n--- All Logs ---")
        for log in self.logs:
            print(log)

# -----------------------------------------
# Payment Service (uses the logger singleton)
# -----------------------------------------
class PaymentService:
    def __init__(self, name):
        self.name = name
        self.logger = Logger.get_instance()

    def make_payment(self, user, amount):
        self.logger.log(f"[{self.name}] Processed payment of ₹{amount} for user {user}.")

# -----------------------------------------
# Application Configuration (singleton too)
# -----------------------------------------
class AppConfig:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance.settings = {
                "currency": "INR",
                "max_retries": 3,
                "mode": "production"
            }
        return cls._instance

    def get_setting(self, key):
        return self.settings.get(key)

# -----------------------------------------
# Test Client Code
# -----------------------------------------
if __name__ == "__main__":
    service1 = PaymentService("Razorpay")
    service2 = PaymentService("Paytm")

    service1.make_payment("Krunal", 1000)
    service2.make_payment("Ravi", 500)

    # Logger is same across services
    Logger.get_instance().show_all_logs()

    # Config is singleton
    config = AppConfig()
    print("\nApp is running in:", config.get_setting("mode"))




# 🧠 Key Features
# ✅ Thread-Safe with threading.Lock()
# ✅ Lazy Initialization – object created only when needed
# ✅ Global Access Point via get_instance()
# ✅ Reuses instance across entire application