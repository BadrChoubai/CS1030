def one_to_ten() -> list:
    numbers: list = []
    while len(numbers) < 10:
        numbers.append(len(numbers) + 1)

    print(numbers)
    
def _range() -> list:
    numbers: list = []
    range_start = int(input("Starting number: "))
    range_end = int(input("Ending number:  "))
    while range_start <= range_end:
        numbers.append(range_start)
        range_start += 1

    return numbers

def reduce_sum(numbers: list) -> int:
    i = 0
    result = 0
    while i < len(numbers):
            result += numbers[i]
            i += 1

    return result

def sum_range() -> int:
    return reduce_sum(_range())

def triangle():
    size = int(input("How big should I be? "))
    for i in range(0, size):
        print('*' * i) 

if __name__ == "__main__":
    triangle()
