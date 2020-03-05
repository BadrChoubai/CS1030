def get_user_input() -> list:
    numbers = []
    
    while len(numbers) < 3:
        number = input("Give me a number: ")
        if number.isdigit():
            numbers.append(int(number))
        else:
            print("You didn't enter a number... and now you don't know what you missed out on.")
            break

        if len(numbers) == 3:
            print(f'You win { sum(numbers) } candies')

if __name__ == "__main__":
    get_user_input()
