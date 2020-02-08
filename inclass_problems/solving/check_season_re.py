def check_season_re(month: str) -> str:
    month = month.lower()

    seasons = {
        "Spring": ["march", "april", "may"],
        "Summer": ["june", "july", "august"],
        "Fall": ["september", "october", "november"],
        "Winter": ["december", "january", "february"]
    }


    def season_for(search_month, seasons=seasons):
        pass 


    return season_for(month)

if __name__ == "__main__":
    print(check_season_re("march"))
    print(check_season_re("august"))
    print(check_season_re("september"))
    print(check_season_re("february"))
