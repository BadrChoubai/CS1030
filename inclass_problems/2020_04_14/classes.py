# Python Object-Oriented Programming


class Employee():
    def __init__(self, first_name: str, last_name: str, position: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary
        self.email = f'{first_name}{last_name}@company.com'

    def full_name(self):
        print(f'{self.first_name} {self.last_name}')


employee_1 = Employee("Badr", "Choubai", "Software Engineer", 70_000)

employee_1.full_name()
