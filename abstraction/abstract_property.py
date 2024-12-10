from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def sides(self):
        pass


class Triange(Shape):
    @property
    def sides(self):
        return 3


triangle = Triange()
print(triangle.sides)

