# Based on the student class you created in problem one, create three class variables,
# ones that apply to ALL students not to an instance
import datetime


class Student():
    school_name = 'Metropolitan State University of Denver'
    students = 0

    def __init__(self, birthday: str, first_name: str, last_name: str, major: str):
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.student_email = f'{first_name}{last_name}@school.edu'

        Student.students += 1

    def full_name(self):
        print(f'{self.first_name} {self.last_name}')


student = Student(datetime.date(1999, 3, 2), "Badr",
                  "Choubai", "Computer Science B.A.")

student.full_name()
print(student.birthday)
print(student.school_name)
