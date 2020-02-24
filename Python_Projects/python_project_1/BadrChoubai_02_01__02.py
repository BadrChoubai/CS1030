"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project One
"""


def get_user_input(prompts: list) -> list:
    prompt_answers: list = []

    for prompt_message in prompts:
        answer = input(f"{ prompt_message }: ")
        prompt_answers.append(int(answer.strip()))

    return prompt_answers


def main():
    prompts: list = ["Enter miles travelled",
                     "Gallons of fuel used? "]

    miles, gallons = get_user_input(prompts)

    kilometers = (miles * 1.60934)
    liters = (gallons * 3.7854)

    miles_per_gallon = (miles / gallons)
    kilometers_per_mile = (kilometers / miles)
    gallons_per_liter = (gallons / liters)

    liters_per_kilometer = 1 / \
        (miles_per_gallon * kilometers_per_mile * gallons_per_liter)

    mpg_str = f"{miles_per_gallon:.2f} mpg"
    lpk_str = f"{liters_per_kilometer:.2f} lpk"

    output_str = f"Miles Per Gallon: {mpg_str} \nLiters Per Kilometer: {lpk_str}"

    print(output_str)


if __name__ == "__main__":
    main()
