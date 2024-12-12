from employee import Employee


class PermanentEmployee(Employee):
    def __init__(self, id: int, name : str, age : int, department : str, base_salary : float, bonus : float):
        super().__init__(id, name, age, department)
        self.bonus = bonus
        self.base_salary = base_salary

    def calculate_salary(self):
        self.set_salary(self.base_salary + self.bonus)
