def fizzBuzz():
    for i in range(0, 101):
        if (i % 15 == 0):
            print("Fizz Buzz")
        elif (i % 5 == 0):
            print("Buzz")
        elif (i % 3 == 0):
            print("Fizz")
        else:
            print(i)

if __name__ == "__main__":
    fizzBuzz()
