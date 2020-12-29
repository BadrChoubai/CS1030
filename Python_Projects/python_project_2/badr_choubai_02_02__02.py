"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Two
"""
from functools import reduce
from random import choice


def get_results(simulations: list) -> tuple:
    min_flips = len(min(simulations))
    max_flips = len(max(simulations))
    average_flips = reduce(lambda x, y: x + y, [len(simulation) for simulation in simulations]) // len(simulations)

    return min_flips, average_flips, max_flips


def simulate(times: int) -> list:
    simulations = []
    while len(simulations) < times:
        current_simulation = []

        while not ('T' * 3 in "".join(current_simulation[-3:]) or 'H' * 3 in "".join(current_simulation[-3:])):
            current_simulation.append(choice(('T', 'H')))

        simulations.append(current_simulation)

    return simulations


def main():
    playing: bool = True

    while playing:
        try:
            times = input("How many times would you like to flip the coin?\n> ")
            times = int(times)
        except ValueError:
            print("Please type in a number value")

        simulations = simulate(times)
        (_min, avg, _max) = get_results(simulations)

        for simulation in simulations:
            print(f"Flips in series: {len(simulation)}")
            print(f"Triplet string: {''.join(simulation[-3:]).upper()}")
            print(f"Result string: {' '.join(simulation)}\n")

        print(f""
              f"minimum number of flips: {_min}\n"
              f"average number of flips: {avg}\n"
              f"maximum number of flips: {_max}\n"
              f"")

        answer: str = input("Would you like to play again?\n> ")
        playing = True if (answer == 'yes' or answer == 'y') else False
    else:
        exit()


if __name__ == "__main__":
    main()
