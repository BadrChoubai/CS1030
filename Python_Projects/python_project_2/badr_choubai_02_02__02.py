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

    2.8 Print the average number of flips, the minimum number of flips and maximum number of flips.

    2.9 Resume at step 2.1.
"""


def flip_coin() -> str:
    from random import choice

    coin = ('H', 'T')
    return choice(coin)


def is_valid_series(series: list) -> bool:
    series = ''.join(series)
    valid = ('TTT' in series or 'HHH' in series)
    return valid


def print_series_results(flips_total: int, series: list):
    print(f"""
    Flips Total: { flips_total };
    Triplet String: { ''.join(series) }
    Results String: TODO
    """)


def main():
    simulations = input(
        "How many coin flipping simulations would you like to run?: ")
    simulations = int(simulations)

    flips_total = 0
    series: list = []

    while simulations > 0:

        while len(series) < 3:
            series.append(flip_coin())
            flips_total += 1

        if is_valid_series(series):
            print_series_results(flips_total, series)
            series.clear()
            flips_total = 0
            simulations -= 1
        else:
            series.clear()


if __name__ == "__main__":
    main()
