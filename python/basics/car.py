from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("car started")
        
    def stop(self):
        print("car stopped")

c= Car()
c.start()
c.stop()
    