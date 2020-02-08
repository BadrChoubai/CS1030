# This solution uses an If statement to return the proper season

def check_season(month: str) -> str:
    month = month.lower()
    season = None

    if  month == 'march' or month == 'april' or month ==  'may': 
        season = "spring"
    elif month == 'june' or month == 'july' or month =='august':
        season = "summer"
    elif month == 'september' or month == 'october' or month == 'november':
        season = "fall"
    elif month == 'december' or month == 'january' or month == 'february':
       season = "winter"

    return season

if __name__ == "__main__":
    print(check_season("march"))
    print(check_season("august"))
    print(check_season("september"))
    print(check_season("february"))
