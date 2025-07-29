# You have a 2-pin plug, but the wall socket is 3-pin.
# → Use an adapter to make them compatible.


# You want to use an existing class, but its interface doesn't match your needs.

# You work with 3rd-party APIs.


# You are building a payment processing system, but one vendor uses a different API (send_money(amount)), and you expect pay(amount).



# Adaptee (incompatible third-party API)
class OldPaymentGateway:
    def send_money(self, amount):
        print(f"Sending ₹{amount} using OldPaymentGateway")

# Target interface expected by your system
class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError

# Adapter
class PaymentAdapter(PaymentProcessor):
    def __init__(self, old_gateway):
        self.old_gateway = old_gateway

    def pay(self, amount):
        self.old_gateway.send_money(amount)

# Your system
def checkout(payment_method: PaymentProcessor, amount):
    print("Processing checkout...")
    payment_method.pay(amount)

# Usage
old_gateway = OldPaymentGateway()
adapter = PaymentAdapter(old_gateway)
checkout(adapter, 1500)
