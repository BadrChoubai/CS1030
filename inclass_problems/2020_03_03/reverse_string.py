def reverse_string(string: str) -> str:
    result = ""
    for i, _ in enumerate(string):
        result += string[len(string) - 1 - i]

    return result 

print(reverse_string("Badr Choubai"))

