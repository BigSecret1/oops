"""
Even though Robot is unrelated to Dog or Cat, the communicate function works because
Robot implements a speak method.
"""
class Dog:
    def speak(self):
        return "Bark"


class Cat:
    def speak(self):
        return "Meow"


class Robot:
    def speak(self):
        return "Beep Beep"


def communication(entitiy):
    print(entitiy.speak())


communication(Dog())
communication(Cat())
communication(Robot())


