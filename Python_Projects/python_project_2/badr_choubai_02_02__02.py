"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Two
"""
from functools import reduce
from random import choice


def calculate_end_results(flips_results: list) -> tuple:
    def _sum(x, y): return x + y

    minimum = min(flips_results)
    average = reduce(_sum, flips_results) // len(flips_results)
    maximum = max(flips_results)
    return (minimum, average, maximum)


def flip_coin() -> str:
    coin = ('H', 'T')
    return choice(coin)


def is_valid_series(section: str) -> bool:
    valid = ('TTT' in section or 'HHH' in section)
    return valid


def print_series_results(result: dict):
    flips, series_string = result.values()
    print(f'''
    Flips In Series: { flips };
    Triplet String:  { series_string[-3:] };
    Results String: { series_string.replace('', ' ', len(series_string)) }; 
    ''')


def main():
    simulations = input(
        "How many coin flipping simulations would you like to run?: ")

    if simulations.isdigit() and int(simulations) > 0:
        simulations = int(simulations)
    else:
        exit()

    flips_results: list = []
    while simulations > 0:
        simulation_result = {
            'flips': 0,
            'series_string': ''
        }
        while not is_valid_series(simulation_result['series_string'][-3:]):
            simulation_result['series_string'] += flip_coin()
            simulation_result['flips'] += 1

        print_series_results(simulation_result)
        flips_results.append(simulation_result['flips'])
        simulations -= 1

    minimum, average, maximum = calculate_end_results(flips_results)
    print(f"""
    Statistics on finding valid Triplet:

    Minimum Number of Flips: { minimum };
    Average Number of Flips: { average };
    Maximum Number of Flips: { maximum };
    """)
    main()


if __name__ == "__main__":
    main()
