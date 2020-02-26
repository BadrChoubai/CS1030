def mutation_math(number: int) -> int:
    """mutation_math
    Write a function that takes a number and return a math equation mutating the number
    Ex. number = 1; return 1 + 11 + 111 -> 123 
    """
    mutation = [int(str(number) * i) for i in range(1, 4)]
    return sum(mutation)
