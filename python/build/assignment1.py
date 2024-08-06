from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def checkAge(self,age):
        pass
    
    @abstractmethod
    def checkEmail(self,email):
        pass
    
class Service(ABC):
    @abstractmethod
    def callService(self, number):
        pass
    
    @abstractmethod
    def messageServices(self, number):
        pass

class Payment(ABC):
    @abstractmethod
    def makePayment(self,amount):
        pass

class PostPaid(Service):
    def callService(self, number):
        print(f"Postpaid Call Services available on {number}")
    
    def messageServices(self, number):
        print(f"Postpaid Message services available on {number}")

class PrePaid(Service):
    def callService(self, number):
        print(f"Prepaid Call Services available on {number}")
    
    def messageServices(self, number):
        print(f"Prepaid Message services available on {number}")

class Cash(Payment):
    def makePayment(self, amount):
        print(f"Cash payment of {amount} is done.")

class Online(Payment):
    def makePayment(self, amount):
        print(f"Online payment of {amount} is done.")        
        
class Employee(Person):
    def checkAge(self, age):
        if age>18:
            print("Right age")
        else:
            print("Too young")
    
    def checkEmail(self, email):
        print(f"{email} Email is correct")
    
    def checkService(self, prepaid_service):
        prepaid_service.callService("8296247970")
    
    def checkPayment(self, onlinePayment):
        onlinePayment.makePayment(100)

pp = PrePaid()
e = Employee()
e.checkService(pp)