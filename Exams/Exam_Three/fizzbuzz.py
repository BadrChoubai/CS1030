def fizzbuzz(n):
    fizz = 'fizz' if n % 3 == 0 else ''
    buzz = 'buzz' if n % 5 == 0 else ''
    fizbuz = 'fizzbuzz' if fizz and buzz else ''

    return fizbuz or buzz or fizz or n


def recurse_fizzbuzz(start, end):
    print(fizzbuzz(start))

    return None if start == end else recurse_fizzbuzz(start+1, end)


recurse_fizzbuzz(start=1, end=100)
