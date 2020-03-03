def sum_even():
    num_one = input("start: ")
    num_two = input("end: ")

    return sum([i for i in range(int(num_one), int(num_two)) if i % 2 == 0])

print(sum_even())
