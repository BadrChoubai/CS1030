from typing import List


def dictionary_builder(key_values: List[tuple]) -> dict:
    if len(key_values) == 0:
        return None

    dictionary = {}
    for key, values in key_values:
        if key not in dictionary:
            dictionary[key] = values

    return dictionary
