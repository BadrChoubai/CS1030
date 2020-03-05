# Write a program that takes a student's name and course number 
# Print a string of "Welcome, { name } to course { course_name }"

def get_student_details():
    name = input("What is your name?: ")
    course_name = input("Course Name: ")

    print(f"Welcome, { name } to course { course_name }")

if __name__ == "__main__":
    get_student_details()
