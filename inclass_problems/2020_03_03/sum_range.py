def sum_range() -> int:
    num_one = input("Enter a starting number: ")
    num_two = input("Enter an ending number: ")
    result = 0 

    for i in range(int(num_one), int(num_two) + 1):
        result += i

    print(result)
    return result


sum_range()
