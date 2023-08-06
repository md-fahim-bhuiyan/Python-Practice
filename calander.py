import calendar
year = 2023
month = '06'
print(calendar.month(year, int(month)))
year = 2023
year2 =2025
print(calendar.calendar(year))
print(calendar.calendar(year2))

calendar_html = calendar.HTMLCalendar().formatyear(year)

with open('calendar.html', 'w') as file:
    file.write(calendar_html)

