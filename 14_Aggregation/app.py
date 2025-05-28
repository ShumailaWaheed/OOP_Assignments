# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def show_info(self):
        print(f"Department: {self.department_name}, Employee: {self.employee.name}")

emp = Employee("Ali")
dept = Department("HR", emp)
dept.show_info()
