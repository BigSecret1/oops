from rich.jupyter import display

from employee import Employee
from typing import List


class Department:
    def __init__(self, id : int, name : str):
        self.id = id
        self.name = name
        self.employees : List[Employee] = []

    def add_employee(self, employee : Employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} has been added to {employee.department} deparment")

    def remove_employee(self, employee_id : int):
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                print(f"\nEmployee {employee.name} has been removed from the deparment")
            else:
                print(f"\nNo employee found with the name {employee.name} in the deparment")

    def display_employees(self):
        print(f"\n Employees in the {self.name} Department")
        if not self.employees:
            print(f"There are no employess in the department")
        for employee in self.employees:
            employee.display_details()
