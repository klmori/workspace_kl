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
        raise NotImplementedError()


class PaytmBankingSystem(BankingSystem):
    def process_payment(self, amount):
        return random.randint(0, 99) < 80  # 80% success rate


class RazorpayBankingSystem(BankingSystem):
    def process_payment(self, amount):
        print(f"[BankingSystem-Razorpay] Processing payment of {amount}...")
        return random.randint(0, 99) < 90  # 90% success rate


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
        raise NotImplementedError()

    def initiate_payment(self, request: PaymentRequest):
        raise NotImplementedError()

    def confirm_payment(self, request: PaymentRequest):
        raise NotImplementedError()


# ----------------------------
# Concrete Payment Gateway for Paytm
# ----------------------------
class PaytmGateway(PaymentGateway):
    def __init__(self):
        super().__init__()
        self.banking_system = PaytmBankingSystem()

    def validate_payment(self, request):
        print(f"[Paytm] Validating payment for {request.sender}.")
        return request.amount > 0 and request.currency == "INR"

    def initiate_payment(self, request):
        print(f"[Paytm] Initiating payment of {request.amount} {request.currency} for {request.sender}.")
        return self.banking_system.process_payment(request.amount)

    def confirm_payment(self, request):
        print(f"[Paytm] Confirming payment for {request.sender}.")
        return True


# ----------------------------
# Concrete Payment Gateway for Razorpay
# ----------------------------
class RazorpayGateway(PaymentGateway):
    def __init__(self):
        super().__init__()
        self.banking_system = RazorpayBankingSystem()

    def validate_payment(self, request):
        print(f"[Razorpay] Validating payment for {request.sender}.")
        return request.amount > 0

    def initiate_payment(self, request):
        print(f"[Razorpay] Initiating payment of {request.amount} {request.currency} for {request.sender}.")
        return self.banking_system.process_payment(request.amount)

    def confirm_payment(self, request):
        print(f"[Razorpay] Confirming payment for {request.sender}.")
        return True


# ----------------------------
# Proxy class that wraps a PaymentGateway to add retries (Proxy Pattern)
# ----------------------------
class PaymentGatewayProxy(PaymentGateway):
    def __init__(self, real_gateway: PaymentGateway, retries: int):
        self.real_gateway = real_gateway
        self.retries = retries

    def process_payment(self, request: PaymentRequest):
        for attempt in range(self.retries):
            if attempt > 0:
                print(f"[Proxy] Retrying payment (attempt {attempt + 1}) for {request.sender}.")
            if self.real_gateway.process_payment(request):
                return True
        print(f"[Proxy] Payment failed after {self.retries} attempts for {request.sender}.")
        return False

    def validate_payment(self, request):
        return self.real_gateway.validate_payment(request)

    def initiate_payment(self, request):
        return self.real_gateway.initiate_payment(request)

    def confirm_payment(self, request):
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
        if GatewayFactory._instance is not None:
            raise Exception("This is a singleton!")
        GatewayFactory._instance = self

    @staticmethod
    def get_instance():
        if GatewayFactory._instance is None:
            GatewayFactory()
        return GatewayFactory._instance

    def get_gateway(self, gateway_type: GatewayType):
        if gateway_type == GatewayType.PAYTM:
            return PaymentGatewayProxy(PaytmGateway(), 3)
        else:
            return PaymentGatewayProxy(RazorpayGateway(), 1)


# ----------------------------
# Unified API service (Singleton)
# ----------------------------
class PaymentService:
    _instance = None

    def __init__(self):
        if PaymentService._instance is not None:
            raise Exception("This is a singleton!")
        self.gateway = None
        PaymentService._instance = self

    @staticmethod
    def get_instance():
        if PaymentService._instance is None:
            PaymentService()
        return PaymentService._instance

    def set_gateway(self, gateway: PaymentGateway):
        self.gateway = gateway

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
        if PaymentController._instance is not None:
            raise Exception("This is a singleton!")
        PaymentController._instance = self

    @staticmethod
    def get_instance():
        if PaymentController._instance is None:
            PaymentController()
        return PaymentController._instance

    def handle_payment(self, gateway_type: GatewayType, request: PaymentRequest):
        gateway = GatewayFactory.get_instance().get_gateway(gateway_type)
        service = PaymentService.get_instance()
        service.set_gateway(gateway)
        return service.process_payment(request)


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    req1 = PaymentRequest("Aditya", "Shubham", 1000.0, "INR")
    print("Processing via Paytm")
    print("------------------------------")
    res1 = PaymentController.get_instance().handle_payment(GatewayType.PAYTM, req1)
    print("Result:", "SUCCESS" if res1 else "FAIL")
    print("------------------------------\n")

    req2 = PaymentRequest("Shubham", "Aditya", 500.0, "USD")
    print("Processing via Razorpay")
    print("------------------------------")
    res2 = PaymentController.get_instance().handle_payment(GatewayType.RAZORPAY, req2)
    print("Result:", "SUCCESS" if res2 else "FAIL")
    print("------------------------------")
