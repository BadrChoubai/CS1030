# Create a student class with 5 instance variables useful for a student
import datetime


class Student():
    def __init__(self, birthday: str, first_name: str, last_name: str, major: str):
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.student_email = f'{first_name}{last_name}@school.edu'

    def full_name(self):
        print(f'{self.first_name} {self.last_name}')


student = Student(datetime.date(1999, 3, 2), "Badr",
                  "Choubai", "Computer Science B.A.")

student.full_name()
print(student.birthday)
