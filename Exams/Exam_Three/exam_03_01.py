months = [
    (31, ['january', 'march', 'may', 'july', 'august', 'october', 'december']),
    (30, ['april', 'june', 'september', 'november']),
    ('28 or 29 days', ['February'])
]

month = input('Enter a month of the year: ')

month = month.lower()
days_in_month = None
for days, months in months:
    if month in months:
        days_in_month = days

print(f'There are {days_in_month} days in {month.title()}')
