# Python Object-Oriented Programming


class Employee():
    number_of_employees = 0
    raise_percentage = 1.04

    def __init__(self, first_name: str, last_name: str, position: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary
        self.email = f'{first_name}{last_name}@company.com'

        # This will help us keep track of how many Employee instances we have created
        Employee.number_of_employees += 1

    def full_name(self):
        print(f'{self.first_name} {self.last_name}')

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percentage)


employee_1 = Employee("Badr", "Choubai", "Software Engineer", 70_000)

employee_1.full_name()
print(employee_1.salary)
employee_1.apply_raise()
print(employee_1.salary)
