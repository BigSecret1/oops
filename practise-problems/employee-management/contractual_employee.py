from employee import Employee


class ContractualEmployees(Employee):
    def __init__(self, id : int, name: str, age : int, department : str, per_hour_pay : float, hours_worked : int):
        super().__init__(id, name, age, department)
        self.per_hour_pay = per_hour_pay
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self.set_salary(self.per_hour_pay * self.hours_worked)

