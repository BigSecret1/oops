from abc import ABC, abstractmethod


class Employee:
    def __init__(self, id : int, name : str, age : int, department: str):
        self.id = id
        self.name = name
        self.age = age
        self.department = department
        self._salary : float = 0

    def calculate_salary(self):
          pass

    def get_salary(self):
        return self._salary

    def set_salary(self, amount : float):
        if amount >= 0:
            self._salary += amount
        else:
            ValueError("Salary can't be negative")

    def display_details(self):
        print(f"\nID : {self.id} Name : {self.name} Age : {self.age} Department : {self.department} Salary : {self.get_salary()}")