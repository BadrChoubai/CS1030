import random


def unique(lottery_numbers: list) -> bool:
    return sum(set(lottery_numbers)) == sum(lottery_numbers)


lottery_numbers = [random.randint(1, 49) for i in range(6)]

while not unique(lottery_numbers):
    lottery_numbers = [random.randint(1, 49) for i in range(6)]

print(sorted(lottery_numbers))
