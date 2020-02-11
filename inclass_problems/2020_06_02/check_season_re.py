# This solution iterates through a dict of seasons

def check_season_re(month: str) -> str:
    month = month.lower()

    seasons = {
        "Spring": ["march", "april", "may"],
        "Summer": ["june", "july", "august"],
        "Fall": ["september", "october", "november"],
        "Winter": ["december", "january", "february"]
    }

    for season, months in seasons.items():
        if month in months:
            return season
        

if __name__ == "__main__":
    print(check_season_re("march"))
    print(check_season_re("august"))
    print(check_season_re("september"))
    print(check_season_re("february"))
