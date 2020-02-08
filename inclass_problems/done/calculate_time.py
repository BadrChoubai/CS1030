def calculate_time(seconds: int) -> str:
    seconds = int(seconds)
    hours, minutes = (int(seconds / 60), seconds % 60)  
    time_as_prompt = str(f"There are { hours } hours and { minutes } minutes remaining")

    return time_as_prompt 

if __name__ == "__main__":
    seconds = int(input("Give me a length of time as seconds: "))
    print(calculate_time(seconds))
