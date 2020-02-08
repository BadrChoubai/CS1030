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



def get_user_input(prompts: list) -> list:
    prompt_answers = [None]*len(prompts)

    for i, prompt_message in enumerate(prompts):
        answer = input(str(f"{ prompt_message }: "))
        prompt_answers[i] = int(answer.strip())

    return prompt_answers


def main():
    prompts: list = ["Enter miles travelled",
                     "Gallons of fuel used? "]

    [miles, gallons] = get_user_input(prompts) 

    kilometers = (miles * 1.60934)
    liters = (gallons * 3.7854)

    miles_per_gallon = (miles / gallons)
    kilometers_per_mile = (kilometers / miles)
    gallons_per_liter = (gallons / liters)

    liters_per_kilometer = 1 / \
        (miles_per_gallon * kilometers_per_mile * gallons_per_liter)

    mpg_str = str(f"{miles_per_gallon:.2f} mpg")
    lpk_str = str(f"{liters_per_kilometer:.2f} lpk")

    output_str = str(
        f"Miles Per Gallon: {mpg_str} \nLiters Per Kilometer: {lpk_str}")

    return output_str


if __name__ == "__main__":
    result = main()
    print(result)
