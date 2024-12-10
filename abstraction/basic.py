from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Barks"

    def sleep(self):
        return "Dog is sleeping"


class Cat(Animal):
    def sound(self):
        return "meow"

    def sleep(self):
        return "Cat is sleeping"


animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
    print(animal.sleep())