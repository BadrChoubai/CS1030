"""
    # 2.1 Ask the user how many simulations they want to run, say N. If the user presses the <Enter> key or enters 0 or a negative number, exit the program.

    # 2.2 Loop N times.

    2.3 Loop until you find three heads or three tails in a row, HHH or TTT, respectively.

    2.4 Start flipping coins. Use randint(1,2) to generate a 1 or 2 for heads and tails respectively.
        - I chose to implement 'choice' from the random module

    2.5 Count flips and check for HHH or TTT.

    2.6 When you get HHH or TTT, print the flips in the current simulation and accumulate the number of flips, minimum number of flips to get three in a row and the highest number of flips to get three in a row. The flips should be displayed with Hs and Ts with a space between each flip, like H T T H H H
        
        choice = choice(('H', 'T'))    
        Something like ''.join(f'{ choice } ') 

    # 2.7 Go on to the next simulation, if there is one.

    2.8 Print the average number of flips, the minimum number of flips and maximum number of flips.

    2.9 Resume at step 2.1.
"""
from random import choice


def flip_coin() -> str:
    coin = ('H', 'T')
    return choice(coin)


def is_valid_series(section: str) -> bool:
    valid = ('TTT' in section or 'HHH' in section)
    return valid


def print_series_results(flips_in_series: int, series: str):
    print(f'''
    Flips In Series: { flips_in_series };
    Triplet String:  { series[-3:] };
    Results String: { series.replace('', ' ', len(series)) }; 
    ''')


def main():
    simulations = input(
        "How many coin flipping simulations would you like to run?: ")
    simulations = int(simulations)
    flips_total = 0

    while simulations > 0:
        series_str = ""
        flips_in_series = 0
        while not is_valid_series(series_str[-3:]):
            series_str += flip_coin()
            flips_in_series += 1

        print_series_results(flips_in_series, series_str)
        flips_total += flips_in_series
        simulations -= 1

    print(f"Total Flips in Simulation: { flips_total }")


if __name__ == "__main__":
    main()
