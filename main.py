class Employee:
    def __init__(self, name: str, age : int, id : int):
        self.name = name
        self.age = age
        self.id = id
        self.company_name = "Apple"

    def __str__(self):
        return (f"Employee name : {self.name} Age : {self.age} Id : {self.id} works in {self.company_name}")


employee = Employee("Dinesh", 26, 341234)
print(employee)
