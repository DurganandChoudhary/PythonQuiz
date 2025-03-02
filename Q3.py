'''
Create a base class Employee with attributes name, emp_id, salary, department.
Implement methods:

__str__ to return employee details.
apply_bonus() to increase salary by a percentage.
show_details() to display employee details.
From Employee, inherit:

Manager with an extra attribute team_size.
Developer with an extra attribute programming_language.

'''


class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department
    
    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: ${self.salary}"
    
    def apply_bonus(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print(f"New salary after {percentage}% bonus: ${self.salary:.2f}")
    
    def show_details(self):
        print(self)

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department, team_size):
        super().__init__(name, emp_id, salary, department)
        self.team_size = team_size
    
    def __str__(self):
        return super().__str__() + f", Team Size: {self.team_size}"
    
    def show_details(self):
        print(self)

class Developer(Employee):
    def __init__(self, name, emp_id, salary, department, programming_language):
        super().__init__(name, emp_id, salary, department)
        self.programming_language = programming_language
    
    def __str__(self):
        return super().__str__() + f", Programming Language: {self.programming_language}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    manager = Manager("Alice Johnson", 101, 80000, "HR", 10)
    developer = Developer("Bob Smith", 102, 70000, "IT", "Python")
    
    manager.show_details()
    developer.show_details()
    
    developer.apply_bonus(10)
    developer.show_details()
