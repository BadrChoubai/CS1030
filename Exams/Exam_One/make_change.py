def make_change(cents: int) -> dict:
    coins = (('quarter', 25), ('nickel', 10), ('dime', 5), ('penny', 1))
    counter = {'quarter': 0, 'nickel': 0, 'dime': 0, 'penny': 0}

    while cents > 0:
        for coin, value in coins:
            if cents - value >= 0:
                counter[coin] += 1
                cents -= value

    return counter
