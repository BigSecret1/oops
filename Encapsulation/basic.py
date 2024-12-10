# this is an example fo protected access modifier
class Car:
    def __init__(self, brand, model, engine):
            self._brand = brand
            self._model = model
            self._engine = engine

    def _display_engine_info(self):
        return f"Enngine: {self._engine}"

    def display_info(self):
        return f"{self._brand} {self._model} {self._display_engine_info()}"


class ElectricCar(Car):
    def display_electric_info(self):
        return f"Electric Car : {self._brand} {self._model}"


car = ElectricCar("Tesla", "Mode 8", "Electric rocket")
print(car.display_info())
print(car.display_electric_info())


#This class demonstrate use of protected access modifer
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def __display_balance(self):
        return f"Balance : {self.__balance}"

    def get_account_details(self):
        return f"Account Number : {self.__account_number}, {self.__display_balance()}"


account = BankAccount("1234", "188888888")
print(account.get_account_details())


class SecondBankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance can't be negative")
        else:
            self.__balance += amount


account = SecondBankAccount("1234234", 123423432)
print(account.get_balance())
account.set_balance(1234132)
print(account.get_balance())
account.set_balance(-2423)

