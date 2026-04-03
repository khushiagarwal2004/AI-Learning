# abstraction is hiding the internal implementation details of a class and show only the essential features to the user
# Here start and stop are abstract methods which are called by another subclass of parent class
# and parent class must have atleast one astract method then only it can be comprise as abstract class

from abc import ABC,abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")
    def stop(self):
        print("Bike Stopped")

def vehicle_actions(vehicle: Vehicle):
    vehicle.start()
    vehicle.stop()

car = Car()
bike = Bike()

vehicle_actions(car)
vehicle_actions(bike)

# vehicle=Vehicle() will cause error as we can't instantiate obj of abstract class