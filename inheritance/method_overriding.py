class Car:
    def __init__(self):
        print("In class Car")

    def fuel_type(self):
        print("fuel type is petrol")


class ElectricCar:
    def __init__(self):
        print("In class ElectricCar")

    def fuel_type(self):
        print("fuel type is electric")

car = Car()
car.fuel_type()

electric_car = ElectricCar()
electric_car.fuel_type()