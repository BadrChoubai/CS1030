def mutation_math(n: int) -> int:
    mutation = sum(int(str(n) * i) for i in range(1, 4))
    return mutation
