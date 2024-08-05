from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def buys(self):
        pass

class Employee(ABC):
    @abstractmethod
    def manages(self):
        pass

class Product(ABC):
    @abstractmethod
    def producedBy(self):
        pass
    
class Electronics(Product):
    def producedBy(self):
        print("Sony")
    
class Medicines(Product):
    def producedBy(self):
        print("MedPlus")
        
headphones = Electronics()
headphones.producedBy()