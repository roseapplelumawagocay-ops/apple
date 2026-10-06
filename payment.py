from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("sending", amount, "via Credit Card")


class PayPalPayment(Payment):
    def process_payment(self, amount):
        print("sending", amount, "via PayPal")


class GcashPayment(Payment):
    def process_payment(self, amount):
        print("sending", amount, "via GCash")


methods = [CreditCardPayment(), PayPalPayment(), GcashPayment()]
for m in methods:
    m.process_payment(49.99)