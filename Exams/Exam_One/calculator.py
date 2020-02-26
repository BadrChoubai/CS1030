def calculations():
    """
    Ask a user for two numbers
    Calculate the Average, Product, and Sum of the two numbers
    """
    num_one = input("Give me a number: ")
    num_two = input("Give me another number: ")
    num_one = int(num_one)
    num_two = int(num_two)

    average = (num_one + num_two) / 2
    product = num_one / num_two
    _sum = num_one + num_two

    print(f"""
    Average -> { average }
    Product -> { product }
    Sum -> { _sum }
    """)


calculations()
