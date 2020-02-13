"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030

### Description ###

This is my solution for problem one of three of Python Project One

The Problem:

    Convert a Height to Meters

    # 1.1 Prompt the user for the height and get the value from the user.

    # 1.2 If the user presses just the <Enter> key (i.e., a number of feet that’s an empty string), exit the program. Convert the input to an integer.

    # 1.3 Do the same for the inches. Again, the user pressing just the <Enter> key means exit the program.

    # 1.4 Calculate the total inches from the feet and inches. If the total inches is greater than or equal 96 inches (the equivalent of 8’0 or more), print a message that the person is really tall!

    # 1.5 Convert inches to centimeters. There are exactly 2.54 centimeters per inch.

    # 1.6 Convert the centimeters to meters and centimeters, rounding to two places.

    # 1.7 Print the original height and the equivalent in meters with messages describing each number.

    # 1.8 Exit the program. 

"""


def feet_to_inches(feet: int) -> int:
    return (feet * 12)


def centimeters_to_meters(centimeters: float) -> float:
    return (centimeters / 100)


def calculate_meters(inches: int) -> float:
    return (centimeters_to_meters(inches_to_centimeters(inches)))


def get_user_input(prompts: list) -> list:
    prompt_answers: list = []

    for prompt_message in prompts:
        answer = input(f"{ prompt_message }: ")
        prompt_answers.append(int(answer.strip()))

    return prompt_answers


def inches_to_centimeters(inches: int) -> float:
    return (inches * 2.54)


def main():

    prompts: list = ["Please input your height in feet",
                     "Please input your height in inches"]

    feet, inches = get_user_input(prompts)
    height_str = f"{feet}'-{inches}\""

    inches_total = feet_to_inches(feet) + inches
    meters = calculate_meters(inches_total)

    output_str = f"Original Height Input {height_str} :: Converted to meters {meters:.2f}m"

    print(output_str) if inches_total <= 95 else print("Wow, you're so tall!")


if __name__ == "__main__":
    main()
