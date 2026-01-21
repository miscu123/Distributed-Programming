class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return "Employee: " + self.name + ", Salary: " + str(self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return "Manager: " + self.name + ", Salary: " + str(self.salary) + ", Department: " + self.department


emp = Employee("John", 3000)
mgr = Manager("Alice", 5000, "IT")

print(emp.get_details())
print(mgr.get_details())