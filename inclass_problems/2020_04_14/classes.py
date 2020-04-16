# Python Object-Oriented Programming


class Employee():
    # Class Variables
    number_of_employees = 0
    raise_percentage = 1.04

    def __init__(self, first_name: str, last_name: str, position: str, salary: int):
        # Instance Variables
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary
        self.email = f'{first_name}.{last_name}@company.com'

        # This will help us keep track of how many Employee instances we have created
        Employee.number_of_employees += 1

    # Instance Methods
    def full_name(self):
        return (f'{self.first_name} {self.last_name}')

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percentage)

    @classmethod
    def set_raise_amount(cls, new_raise_percentage):
        cls.raise_percentage = new_raise_percentage

    @classmethod
    def from_string(cls, employee_info_str):
        first_name, last_name, position, salary = employee_info_str.split(',')
        return cls(first_name, last_name, position, int(salary))


employee_1 = Employee("Badr", "Choubai", "Software Engineer", 70_000)
print(employee_1.full_name())

employee_info_str = 'John,Doe,Software Engineer,70000'
new_employee = Employee.from_string(employee_info_str)
print(new_employee.full_name())
