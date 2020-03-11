'''
Using the dictionary you created for problem one, write a program to prompt for a number from 1 to 7 and print the day of the
week associated with that number. If the number provided is not in range of 1-7 print an error message and exit the program.
'''
weeks = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
}

day_selection = input("Give me a number from 1-7: ")

if int(day_selection) in weeks.keys():
    print(f'Selected day of the week -> { weeks[int(day_selection)] }')
else:
    print('Invalid day selection')
    exit()
