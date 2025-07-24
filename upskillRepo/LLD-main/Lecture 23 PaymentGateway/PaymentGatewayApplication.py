import random
from enum import Enum

# ----------------------------
# Data structure for payment details
# ----------------------------
class PaymentRequest:
    def __init__(self, sender, receiver, amount, currency):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.currency = currency

# ----------------------------
# Banking System interface and implementations (Strategy for actual payment logic)
# ----------------------------
class BankingSystem:
    def process_payment(self, amount):
        raise NotImplementedError

class PaytmBankingSystem(BankingSystem):
    def process_payment(self, amount):
        # Simulate 80% success
        r = random.randint(0, 99)
        return r < 80

class RazorpayBankingSystem(BankingSystem):
    def process_payment(self, amount):
        print(f"[BankingSystem-Razorpay] Processing payment of {amount}...")
        # Simulate 90% success
        r = random.randint(0, 99)
        return r < 90

# ----------------------------
# Abstract base class for Payment Gateway (Template Method Pattern)
# ----------------------------
class PaymentGateway:
    def __init__(self):
        self.banking_system = None

    def process_payment(self, request: PaymentRequest):
        if not self.validate_payment(request):
            print(f"[PaymentGateway] Validation failed for {request.sender}.")
            return False
        if not self.initiate_payment(request):
            print(f"[PaymentGateway] Initiation failed for {request.sender}.")
            return False
        if not self.confirm_payment(request):
            print(f"[PaymentGateway] Confirmation failed for {request.sender}.")
            return False
        return True

    def validate_payment(self, request: PaymentRequest):
        raise NotImplementedError
    def initiate_payment(self, request: PaymentRequest):
        raise NotImplementedError
    def confirm_payment(self, request: PaymentRequest):
        raise NotImplementedError

# ----------------------------
# Concrete Payment Gateway for Paytm
# ----------------------------
class PaytmGateway(PaymentGateway):
    def __init__(self):
        super().__init__()
        self.banking_system = PaytmBankingSystem()

    def validate_payment(self, request: PaymentRequest):
        print(f"[Paytm] Validating payment for {request.sender}.")
        if request.amount <= 0 or request.currency != "INR":
            return False
        return True

    def initiate_payment(self, request: PaymentRequest):
        print(f"[Paytm] Initiating payment of {request.amount} {request.currency} for {request.sender}.")
        return self.banking_system.process_payment(request.amount)

    def confirm_payment(self, request: PaymentRequest):
        print(f"[Paytm] Confirming payment for {request.sender}.")
        return True

# ----------------------------
# Concrete Payment Gateway for Razorpay
# ----------------------------
class RazorpayGateway(PaymentGateway):
    def __init__(self):
        super().__init__()
        self.banking_system = RazorpayBankingSystem()

    def validate_payment(self, request: PaymentRequest):
        print(f"[Razorpay] Validating payment for {request.sender}.")
        if request.amount <= 0:
            return False
        return True

    def initiate_payment(self, request: PaymentRequest):
        print(f"[Razorpay] Initiating payment of {request.amount} {request.currency} for {request.sender}.")
        return self.banking_system.process_payment(request.amount)

    def confirm_payment(self, request: PaymentRequest):
        print(f"[Razorpay] Confirming payment for {request.sender}.")
        return True

# ----------------------------
# Proxy class that wraps a PaymentGateway to add retries (Proxy Pattern)
# ----------------------------
class PaymentGatewayProxy(PaymentGateway):
    def __init__(self, real_gateway: PaymentGateway, max_retries: int):
        super().__init__()
        self.real_gateway = real_gateway
        self.retries = max_retries

    def process_payment(self, request: PaymentRequest):
        result = False
        for attempt in range(self.retries):
            if attempt > 0:
                print(f"[Proxy] Retrying payment (attempt {attempt+1}) for {request.sender}.")
            result = self.real_gateway.process_payment(request)
            if result:
                break
        if not result:
            print(f"[Proxy] Payment failed after {self.retries} attempts for {request.sender}.")
        return result

    def validate_payment(self, request: PaymentRequest):
        return self.real_gateway.validate_payment(request)
    def initiate_payment(self, request: PaymentRequest):
        return self.real_gateway.initiate_payment(request)
    def confirm_payment(self, request: PaymentRequest):
        return self.real_gateway.confirm_payment(request)

# ----------------------------
# Gateway Factory for creating gateway (Singleton)
# ----------------------------
class GatewayType(Enum):
    PAYTM = 1
    RAZORPAY = 2

class GatewayFactory:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = GatewayFactory()
        return cls._instance

    def get_gateway(self, type_: GatewayType):
        if type_ == GatewayType.PAYTM:
            payment_gateway = PaytmGateway()
            return PaymentGatewayProxy(payment_gateway, 3)
        else:
            payment_gateway = RazorpayGateway()
            return PaymentGatewayProxy(payment_gateway, 1)

# ----------------------------
# Unified API service (Singleton)
# ----------------------------
class PaymentService:
    _instance = None

    def __init__(self):
        self.gateway = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PaymentService()
        return cls._instance

    def set_gateway(self, g: PaymentGateway):
        self.gateway = g

    def process_payment(self, request: PaymentRequest):
        if self.gateway is None:
            print("[PaymentService] No payment gateway selected.")
            return False
        return self.gateway.process_payment(request)

# ----------------------------
# Controller class for all client requests (Singleton)
# ----------------------------
class PaymentController:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PaymentController()
        return cls._instance

    def handle_payment(self, type_: GatewayType, req: PaymentRequest):
        payment_gateway = GatewayFactory.get_instance().get_gateway(type_)
        PaymentService.get_instance().set_gateway(payment_gateway)
        return PaymentService.get_instance().process_payment(req)

# ----------------------------
# Main: Client code now goes through controller
# ----------------------------
if __name__ == "__main__":
    req1 = PaymentRequest("Aditya", "Shubham", 1000.0, "INR")
    print("Processing via Paytm")
    print("------------------------------")
    res1 = PaymentController.get_instance().handle_payment(GatewayType.PAYTM, req1)
    print(f"Result: {'SUCCESS' if res1 else 'FAIL'}")
    print("------------------------------\n")

    req2 = PaymentRequest("Shubham", "Aditya", 500.0, "USD")
    print("Processing via Razorpay")
    print("------------------------------")
    res2 = PaymentController.get_instance().handle_payment(GatewayType.RAZORPAY, req2)
    print(f"Result: {'SUCCESS' if res2 else 'FAIL'}")
    print("------------------------------")
