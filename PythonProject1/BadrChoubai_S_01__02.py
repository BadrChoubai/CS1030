"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030

### Description ###

This is my solution for problem two of three of Python Project One

The Problem:

    Convert from miles per gallon to liters per kilomete
    
    # 2.1 Prompt the user to enter a figure for miles per gallon.

    # 2.2 If the amount is <= 0, exit the program.

    # 2.3 Convert miles to kilometers and gallons to liters. (Google the formulas.)

    # 2.4 From the previous step, calculate liters per kilometer.

    # 2.5 Print the miles per gallon and liters per kilometer with relevant messages, formatting your results to one decimal place.

    # 2.6 Exit the program. 

"""


def get_user_input(prompt: str) -> str:
    prompt_message = str(f"{ prompt }: ")
    return input(prompt_message)


def main():
    prompts: list = ["Enter miles travelled",
                     "Gallons of fuel used? "]
    prompt_answers: list = [None]*len(prompts)

    for i, prompt in enumerate(prompts):
        answer = get_user_input(prompt)
        answer = int(answer)
        if (answer == "" or answer <= 0):
            exit()
        else:
            prompt_answers[i] = answer

    miles, gallons = prompt_answers

    kilometers = (miles * 1.60934)
    liters = (gallons * 3.7854)

    miles_per_gallon = (miles / gallons)
    kilometers_per_mile = (kilometers / miles)
    gallons_per_liter = (gallons / liters)

    liters_per_kilometer = 1 / \
        (miles_per_gallon * kilometers_per_mile * gallons_per_liter)

    mpg_str = str(f"{miles_per_gallon} mpg")
    lpk_str = str(f"{liters_per_kilometer:.2f} lpk")

    output_str = str(
        f"Miles Per Gallon: {mpg_str} \nLiters Per Kilometer: {lpk_str}")

    return output_str


if __name__ == "__main__":
    result = main()
    print(result)
    exit()
