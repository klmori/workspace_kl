# 🧠 Purpose
# The Factory Pattern is used to encapsulate object creation logic.
# Instead of creating objects directly using new or ClassName(), we delegate the creation to a Factory, which decides which subclass or implementation to instantiate.


# 🏪 Real-Life Analogy: Food Delivery Notification System
# Imagine you are building a Zepto-like app that supports sending notifications:

# If the user is in India → SMS (using a local SMS gateway)

# If the user is overseas → Email

# If the user has push notifications enabled → App Notification

# You don’t want your main code to use new EmailSender() or new SmsSender() directly.

# Instead, a NotificationFactory can take a type or user_profile and return the right notification sender.



from abc import ABC, abstractmethod

# -----------------------------
# Product Interface
# -----------------------------
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str, user: dict):
        pass

# -----------------------------
# Concrete Products
# -----------------------------
class EmailSender(NotificationSender):
    def send(self, message, user):
        print(f"Sending EMAIL to {user['email']}: {message}")

class SmsSender(NotificationSender):
    def send(self, message, user):
        print(f"Sending SMS to {user['phone']}: {message}")

class PushNotificationSender(NotificationSender):
    def send(self, message, user):
        print(f"Sending PUSH notification to user {user['id']}: {message}")

# -----------------------------
# Factory
# -----------------------------
class NotificationFactory:
    @staticmethod
    def get_sender(user: dict) -> NotificationSender:
        if user.get("push_enabled"):
            return PushNotificationSender()
        elif user.get("country") == "India":
            return SmsSender()
        else:
            return EmailSender()

# -----------------------------
# Client Code
# -----------------------------
def notify_user(user: dict, message: str):
    sender = NotificationFactory.get_sender(user)
    sender.send(message, user)

# -----------------------------
# Test Example
# -----------------------------
if __name__ == "__main__":
    users = [
        {"id": 1, "email": "a@example.com", "phone": "9999999999", "country": "India", "push_enabled": False},
        {"id": 2, "email": "b@example.com", "phone": "8888888888", "country": "US", "push_enabled": False},
        {"id": 3, "email": "c@example.com", "phone": "7777777777", "country": "India", "push_enabled": True}
    ]

    for user in users:
        notify_user(user, "Your order has been shipped!")


# 🔍 Benefits of Factory Pattern
# ✅ Centralizes object creation logic
# ✅ Easy to add new types (WhatsAppSender, etc.)
# ✅ Reduces coupling between client code and concrete classes
# ✅ Promotes Open/Closed Principle
# ✅ Ideal when:
# There are multiple implementations of a base interface

# Object creation involves logic or conditions