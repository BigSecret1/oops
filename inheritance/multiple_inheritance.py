class Animal:
    def speak(self):
        print("Animal speaks")


class Mammal:
    def move(self, name):
        print(f"The moving dog name is {name}")


class Dog(Mammal, Animal):
    def bark(self):
        print("Dog barked")

    def move(self, name):
        print("Dog moves too")


dog = Dog()
dog.speak()
dog.move("Sam")
dog.bark()