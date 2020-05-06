shallow_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def shallow_flatten(matrix: list) -> list:
    flat = []
    for _list in matrix:
        for i in _list:
            flat.append(i)

    return flat


print(shallow_flatten(shallow_matrix))

deep_matrix = [
    [[1], 2, 3],
    [4, 5, 6],
    [[7, 8, [9]]]
]


def deeply_flatten(matrix: list) -> list:
    for i in matrix:
        if isinstance(i, (list)):
            for j in deeply_flatten(i):
                yield j
        else:
            yield i


# deeply flatten is called as a generator expression
print(list(deeply_flatten(deep_matrix)))
