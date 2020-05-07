import time
from random import shuffle


def _timer(func):
    def wrap(*args):
        start = time.time()
        ret = func(*args)
        end = time.time()
        print('{:s} function took {:.3f} ms'.format(
            func.__name__, (end-start)*1000.0))
        return ret
    return wrap


@_timer
def bubble_sort(numbers):
    # This is to ensure the loop runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

                swapped = True

    return numbers


def main():
    _list = [i for i in range(1, 1001)]
    shuffle(_list)

    # Bubble Sort
    bubble_sort(_list)


if __name__ == "__main__":
    main()
