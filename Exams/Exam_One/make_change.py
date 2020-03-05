def make_change(cents: int) -> dict:
    coins = (('quarter', 25), ('dime', 10), ('nickel', 5), ('penny', 1))
    counter = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}

    for coin, value in coins:
        while cents - value >= 0: 
            counter[coin] += 1
            cents -= value 

    return counter

