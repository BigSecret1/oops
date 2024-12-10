class Calculator:
    def add(self, a, b = 3, c = 3):
        return a + b + c


calc = Calculator()
print(calc.add(4))
print(calc.add(2, 3))
print(calc.add(2, 3, 4))