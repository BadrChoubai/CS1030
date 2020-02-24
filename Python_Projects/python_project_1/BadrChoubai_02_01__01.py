"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project One
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
        try:
            answer = int(answer)
            prompt_answers.append(answer)
        except ValueError:
            print("Please double check you entered a number")
            exit()

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
