# import calendar
#
# year = 2023
# month = '06'
#
# print(calendar.month(year, int(month)))


# import calendar
#
# year = 2023
#
# print(calendar.calendar(year))


import calendar

year = 2024
calendar_html = calendar.HTMLCalendar().formatyear(year)

with open('calendar.html', 'w') as file:
    file.write(calendar_html)
