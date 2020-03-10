'''
Using the 'week' dictionary from problem one, write code that prints the dictionary's days, one number and day per line.
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

for number, day in weeks.items():
    print(number, day)
