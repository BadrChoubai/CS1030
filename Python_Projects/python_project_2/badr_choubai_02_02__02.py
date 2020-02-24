"""
    # 2.1 Ask the user how many simulations they want to run, say N. If the user presses the <Enter> key or enters 0 or a negative number, exit the program.

    # 2.2 Loop N times.

    # 2.3 Loop until you find three heads or three tails in a row, HHH or TTT, respectively.

    # 2.4 Start flipping coins. Use randint(1,2) to generate a 1 or 2 for heads and tails respectively.
        - I chose to implement 'choice' from the random module

    # 2.5 Count flips and check for HHH or TTT.

    # 2.6 When you get HHH or TTT, print the flips in the current simulation and accumulate the number of flips, minimum number of flips to get three in a row and the highest number of flips to get three in a row. The flips should be displayed with Hs and Ts with a space between each flip, like H T T H H H
        
        choice = choice(('H', 'T'))    
        Something like ''.join(f'{ choice } ') 

    # 2.7 Go on to the next simulation, if there is one.

    # 2.8 Print the average number of flips, the minimum number of flips and maximum number of flips.

    # 2.9 Resume at step 2.1.
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
