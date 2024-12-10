from abc import ABC, abstractmethod


class Vehicle:
    def start(self):
        print("Starting the vehicle")

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Driveing the car...")


car = Car()
car.start()
car.drive()