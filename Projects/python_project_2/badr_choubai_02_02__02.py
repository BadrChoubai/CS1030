'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Two
'''
from functools import reduce
from random import choice


def calculate_end_results(flip_results: list) -> tuple:
    '''
    Args:
        flip_results: flip results from all simulations
    Returns:
        (tuple) of calculated minimum, average and maximum
    '''

    minimum = min(flip_results)
    average = reduce(lambda x, y: x + y, flip_results) // len(flip_results)
    maximum = max(flip_results)
    return (minimum, average, maximum)


def flip_coin() -> str:
    '''
    Returns:
        choice: return random selection of value in coin
    '''
    coin = ('H', 'T')
    return choice(coin)


def is_valid_series(section: str) -> bool:
    '''
    Args:
        section: section of string to validate
    Returns:
        valid: boolean of whether or not valid triplet ('HHH' or 'TTT') was found
    '''
    valid = ('TTT' in section or 'HHH' in section)
    return valid


def series_results(result: dict) -> str:
    '''
    Args:
        result: results for one coin flipping simulation 
    Returns:
        Formatted string with simulation statistics
    '''
    flips, series_string = result.values()
    return f'''
    Flips In Series: { flips };
    Triplet String:  { series_string[-3:] };
    Results String: { series_string.replace('', ' ', len(series_string)) }; 
    '''


def simulation_statistics(flip_results: list) -> str:
    '''
    Args:
        flip_results: flip results from all simulations
    Returns:
        Formatted string with simulation statistics 
    '''
    (minimum, average, maximum) = calculate_end_results(flip_results)
    return f'''
    Statistics on finding valid Triplet:

    Minimum Number of Flips: { minimum };
    Average Number of Flips: { average };
    Maximum Number of Flips: { maximum };
    '''


def main():
    simulations = input(
        'How many coin flipping simulations would you like to run?: ')

    if simulations.isdigit() and int(simulations) > 0:
        simulations = int(simulations)
    else:
        print("Invalid input")
        exit()

    flip_results: list = []
    while simulations > 0:
        simulation_result = {
            'flips': 0,
            'series_string': ''
        }
        while not is_valid_series(simulation_result['series_string'][-3:]):
            simulation_result['series_string'] += flip_coin()
            simulation_result['flips'] += 1

        print(series_results(simulation_result))
        flip_results.append(simulation_result['flips'])
        simulations -= 1

    print(simulation_statistics(flip_results))
    main()


if __name__ == '__main__':
    main()
