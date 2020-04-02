students = [
    'Badr C',
    'Kyle E',
    'Samuel H',
    'Julian M',
    'Abby S',
]

with open('students.txt', 'w') as students_file:
    for student in students:
        students_file.write(student + '\n')

students_file.close()
