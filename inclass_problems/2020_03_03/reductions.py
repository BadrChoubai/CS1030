def _reduce(numbers: [int or float], reducer) -> int or float:
    if len(numbers) > 1:
        numbers[0] = reducer(numbers[0], numbers[1])
        numbers.pop(1)
        return _reduce(numbers, reducer)
    else:
        return numbers[0]


def _sum(x, y):
    return x + y

print(_reduce([1, 2, 3], _sum))
