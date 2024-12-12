from employee import Employee


class PayrollSystem:
    @staticmethod
    def calculate_total_expanditure(departments):
        total : int = 0
        for department in departments:
            for employee in department.employees:
                total += employee.get_salary()
        return total

    @staticmethod
    def generate_payroll_summary(departments):
        print("\nPayroll Summary:")
        for department in departments:
            print(f"\n Deparment name {department.name}")
            if not department.employees:
                print("\n No Employees are there in this department")
            else:
                for employee in department.employees:
                    print(f"Employee: {employee.name}   Salary : {employee.get_salary()}")
        print(f"\nTotal Salary Expanditure: {PayrollSystem.calculate_total_expanditure(departments)}")