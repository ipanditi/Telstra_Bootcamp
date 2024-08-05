from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class GpayGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using Gpay")

class PhonePeGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using PhonePe")
        
class PayForItem:
    def doPayment(self,paymentGateway):
        #paymentGateway is an internal instance of payment gateway
        paymentGateway.process_payment(100)

payment_gateway = GpayGateway()
p=PayForItem()
p.doPayment(payment_gateway)
        
