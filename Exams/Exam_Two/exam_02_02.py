import random


def generate_lottery_numbers():
    lottery_numbers = [0, 0, 0, 0, 0, 0]

    for i, _ in enumerate(lottery_numbers):
        lottery_numbers[i] = random.randint(1, 49)

    return lottery_numbers


lottery_numbers = generate_lottery_numbers()

if len(set(lottery_numbers)) != 6:
    lottery_numbers = generate_lottery_numbers()
else:
    print(sorted(lottery_numbers))
