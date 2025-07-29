# The Chain of Responsibility (CoR) pattern allows multiple objects to handle a request without knowing the handler explicitly. Each handler in the chain decides either to process the request or pass it to the next handler.



# 🧠 Real-Life Analogy: Customer Support System
# Imagine you're contacting customer support.

# First, a chatbot answers → if it can't help →

# Escalates to a junior agent → if still unresolved →

# Escalates to a senior agent.

# Each level decides whether to handle or forward.


from abc import ABC, abstractmethod

# ----------------------------
# Log Levels (Enum-like)
# ----------------------------
DEBUG = 1
INFO = 2
WARNING = 3
ERROR = 4
CRITICAL = 5

# ----------------------------
# Handler Interface
# ----------------------------
class LogHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  # allows chaining

    def handle(self, level, message):
        if self.can_handle(level):
            self.process(message)
        elif self.next_handler:
            print(f"[{self.__class__.__name__}] Passing to next handler...")
            self.next_handler.handle(level, message)
        else:
            print(f"[Unhandled] {message}")

    @abstractmethod
    def can_handle(self, level):
        pass

    @abstractmethod
    def process(self, message):
        pass

# ----------------------------
# Concrete Handlers
# ----------------------------
class DebugLogger(LogHandler):
    def can_handle(self, level):
        return level == DEBUG

    def process(self, message):
        print(f"[DEBUG] {message}")

class InfoLogger(LogHandler):
    def can_handle(self, level):
        return level == INFO

    def process(self, message):
        print(f"[INFO] {message}")

class ErrorLogger(LogHandler):
    def can_handle(self, level):
        return level >= ERROR  # handles ERROR and CRITICAL

    def process(self, message):
        print(f"[ERROR] {message}")

# ----------------------------
# Client
# ----------------------------
def main():
    # Build chain: Debug → Info → Error
    debug = DebugLogger()
    info = InfoLogger()
    error = ErrorLogger()

    debug.set_next(info).set_next(error)

    # Send logs at different levels
    debug.handle(DEBUG, "This is a debug message")
    debug.handle(INFO, "Application started successfully")
    debug.handle(WARNING, "This warning will be ignored")
    debug.handle(ERROR, "Null pointer exception!")
    debug.handle(CRITICAL, "Database connection lost!")

if __name__ == "__main__":
    main()



# 🧰 Real-World Examples
# System	Use Case
# Customer Support	Tiered help desks (bot → agent → manager)
# Logging System	Log filters based on severity
# Event Propagation in UI	Mouse/key events bubbling up widget hierarchy
# Spam Filters	Each filter checks message, then passes it on
# Middleware in Web Framework	Authentication → Logging → Routing
# Payment Retry System	Retry via card → UPI → wallet