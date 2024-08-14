from abc import ABC, abstractmethod
 
# Packing interface
class Packing(ABC):
    @abstractmethod
    def pack(self):
        pass
 
# Wrapper class implementing Packing
class Wrapper(Packing):
    def pack(self):
        return "Wrapper"
 
# Bottle class implementing Packing
class Bottle(Packing):
    def pack(self):
        return "Bottle"
 
# Item interface
class Item(ABC):
    @abstractmethod
    def name(self):
        pass
 
    @abstractmethod
    def packing(self):
        pass
 
    @abstractmethod
    def price(self):
        pass
 
# Burger class implementing Item
class Burger(Item):
    def packing(self):
        return Wrapper()
 
# ColdDrink class implementing Item
class ColdDrink(Item):
    def packing(self):
        return Bottle()
 
# VegBurger class
class VegBurger(Burger):
    def name(self):
        return "Veg Burger"
 
    def price(self):
        return 25.0
 
# ChickenBurger class
class ChickenBurger(Burger):
    def name(self):
        return "Chicken Burger"
 
    def price(self):
        return 50.5
 
# Pepsi class
class Pepsi(ColdDrink):
    def name(self):
        return "Pepsi"
 
    def price(self):
        return 30.0
 
# Coke class
class Coke(ColdDrink):
    def name(self):
        return "Coke"
 
    def price(self):
        return 35.0
 
# Meal class
class Meal:
    def __init__(self):
        self.items = []
 
    def add_item(self, item):
        self.items.append(item)
 
    def get_cost(self):
        return sum(item.price() for item in self.items)
 
    def show_items(self):
        for item in self.items:
            print(f"Item: {item.name()}, Packing: {item.packing().pack()}, Price: {item.price()}")
 
# MealBuilder class
class MealBuilder:
    def prepare_veg_meal(self):
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())
        return meal
 
    def prepare_non_veg_meal(self):
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal
 
# BuilderPatternDemo function
def builder_pattern_demo():
    meal_builder = MealBuilder()
 
    veg_meal = meal_builder.prepare_veg_meal()
    print("Veg Meal")
    veg_meal.show_items()
    print("Total Cost:", veg_meal.get_cost())
 
    non_veg_meal = meal_builder.prepare_non_veg_meal()
    print("\nNon-Veg Meal")
    non_veg_meal.show_items()
    print("Total Cost:", non_veg_meal.get_cost())
 
# Run demo
builder_pattern_demo()