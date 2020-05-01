def odd_or_even(value: int) -> str:
    return ["odd", "even"][value % 2 == 0]


if __name__ == "__main__":
    print(odd_or_even_value(2))
    print(odd_or_even_value(3))
