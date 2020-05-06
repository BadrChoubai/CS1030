from functools import reduce


def increment(num: int) -> int:
    return num + 1


a = 0
a = increment(a)
print(a)

# Don't use for, use map()

lengths = map(len, ['scrabble', 'pythonic', 'functional'])
print(list(lengths))

# Lambda functions

self_exponentiation = map(lambda x: x**x, [1, 3, 5, 7, 9, 11])
print(list(self_exponentiation))

sum_evens = reduce(lambda prv, nxt: prv + nxt, [2, 4, 6, 8, 10])
print(sum_evens)

# filter

odds = filter(lambda x: x % 2, [i for i in range(1, 101)])
print(list(odds))
