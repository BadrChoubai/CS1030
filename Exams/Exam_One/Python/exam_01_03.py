def make_change(cents: int) -> dict:
    counter = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}

    for coin, value in zip(counter.keys(), [25, 10, 5, 1]):
        while cents - value >= 0:
            counter[coin] += 1
            cents -= value

    return counter
