def odd_or_even_value(value: int) -> str:
    return 'Even' if value % 2 == 0 else 'Odd'


if __name__ == "__main__":
    print(odd_or_even_value(2))
    print(odd_or_even_value(3))

