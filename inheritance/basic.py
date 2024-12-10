class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal name is ", name)

    def speak(self):
        print(f"{self.name} making a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.name = "Dog name overridden"

    def speak(self):
        print(f"{self.name} barks")


animal = Animal("Big Animal")
print(animal.name)
animal.speak()

dog = Dog("Zylo", "bull dog")
print(dog.name)
print(animal.name)