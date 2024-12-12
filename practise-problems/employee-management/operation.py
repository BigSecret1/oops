from employee import Employee
from department import Department
from main import \
    employee
from permanent_employee import PermanentEmployee
from contractual_employee import ContractualEmployees
from payroll_system import PayrollSystem


hr_department = Department(1, "HR")
it_department = Department(2, "IT")

employee1 = PermanentEmployee(12342, "Ramesh", 28, "HR", 1234234231.23, 3423)
employee2 = PermanentEmployee(12344, "Abby", 32, "HR", 1234234231.23, 3423)

employee3 = ContractualEmployees(12342, "Alice", 23, "IT", 343423, 11)
employee4 = ContractualEmployees(12312, "Jhon", 23, "IT", 343423, 11)

hr_department.add_employee(employee1)
hr_department.add_employee(employee2)

it_department.add_employee(employee3)
it_department.add_employee(employee4)

hr_department.display_employees()
it_department.display_employees()

employee1.calculate_salary()
employee2.calculate_salary()
employee3.calculate_salary()
employee4.calculate_salary()

departments = [hr_department, it_department]
PayrollSystem.generate_payroll_summary(departments)

hr_department.remove_employee(12344)

hr_department.display_employees()
it_department.display_employees()

