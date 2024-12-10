class Animal:
    def sound(self):
        return "Animal makes sound"


class Dog(Animal):
    def sound(self):
        return "Dog is barking"


class Cat(Animal):
    def sound(self):
        return "Cat meows"


animal = Animal()
print(animal.sound())

dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())
