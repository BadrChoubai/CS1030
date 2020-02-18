# Write a function that returns True/False depending on if a number is positive or negative
def positive_number(num: int) -> bool:
    return True if num > 0 else False

# Write a function that returns True/False depending on if a number is even
def num_even(num: int) -> bool:
    return True if num % 2 == 0 else False

def larger_of_two_values(x, y):
    return x if x >= y else y

def larger_of_three_values(x, y, z):
    largest = x
    if y > largest:
        largest = y
    elif z > largest:
        largest = z

    return largest

if __name__ == "__main__":
    print(positive_number(5))
    print(positive_number(-5))

    print(num_even(10))
    print(num_even(15))

    numbers = larger_of_two_values(5, 9)
    floats = larger_of_two_values(5.0, 9.0)
    strings = larger_of_two_values("Badr", "Choubai")

    print(f"""
    Result of larger_of_two_values()
    Integers: { numbers }
    Floats: { floats }
    Strings: { strings }
    """)
    
    largest_of_three = larger_of_three_values(-12, 12, 2)
    print(f"""
    Result of larger_of_three_values(-12, 12, 2)
    Result == { largest_of_three }

    Result of larger_of_three_values(12, -12, -2)
    Result == { larger_of_three_values(12, -12, -2) }

    Result of larger_of_three_values(-12, -12, 2.0)
    Result == { larger_of_three_values(-12, -12, 2.0) }
    """)
