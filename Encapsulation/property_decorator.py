class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return f"Balance : {self.__balance}"

    @balance.setter
    def balance(self, amount : int):
        if amount < 0:
            raise ValueError("Amount can't negative")
        else:
            self.__balance += amount


bank = BankAccount("12343214", 123432432)
print(bank.balance)
bank.balance = 233
print(bank.balance)