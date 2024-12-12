# Employee Management System

## Problem Statement
You are tasked with designing an Employee Management System for a company using Object-Oriented Programming (OOP) concepts in Python. The system should manage employees, departments, and payroll operations. Utilize abstraction, encapsulation, inheritance, and polymorphism effectively.

## Requirements

### Employees

Each employee has:
- `employee_id`
- `name`
- `age`
- `department`
- `salary`

There are two types of employees:
1. **Permanent Employees**: Have additional benefits like bonuses.
2. **Contractual Employees**: Paid hourly with no bonuses.

**Polymorphism** should be used to calculate salaries differently for permanent and contractual employees.

### Departments

Each department has:
- `department_id`
- `name`
- `employees` (list of employees in the department)

A department can:
- Add employees.
- Remove employees.
- Display all employees.

### Payroll

A payroll system should:
- Calculate the total salary expenditure for all employees.
- Allow the manager to generate a payroll summary.

### Concepts to Use

#### Encapsulation
- Protect sensitive attributes like `salary` to prevent unauthorized access.
- Use getters and setters to manage access to sensitive data.

#### Abstraction
- Define an abstract base class `Employee` that enforces common behavior like calculating salary.

#### Inheritance
- Use inheritance to define `PermanentEmployee` and `ContractualEmployee`.

#### Polymorphism
- Use polymorphism to calculate salaries based on employee type:
  - **Permanent employees** get a base salary plus a bonus.
  - **Contractual employees** are paid hourly.
