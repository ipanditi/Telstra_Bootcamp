from abc import ABC, abstractmethod
class VehicleFactory:
    def create_vehicle(self, type, brand, model):
        if type=='car':
            return Car(brand, model)
        elif type=='truck':
            return Truck(brand, model)
        else:
            raise ValueError(f"Unsupported vehicle type: {type}")

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"Driving a {self.brand} {self.model} car")

class Truck(Vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"Driving a {self.brand} {self.model} truck")

factory = VehicleFactory()
car =  factory.create_vehicle('car','Toyota','Corolla')
truck = factory.create_vehicle('truck','Ashok Leyland','432')

car.drive()
truck.drive()