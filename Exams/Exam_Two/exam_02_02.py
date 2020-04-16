from random import randint

lottery_numbers = list()

for i in range(6):
    number = randint(1, 49)

    while number in lottery_numbers:
        number = randint(1, 49)

    lottery_numbers.append(number)

lottery_numbers.sort()
print(lottery_numbers)
