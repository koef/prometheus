# -*- coding: utf-8 -*-
__author__ = 'koef'
import datetime


def create_calendar_page(month=None, year=None):
    cal = "-"*20 + "\n"
    cal += "MO TU WE TH FR SA SU\n"
    cal += "-"*20 + "\n"

    if month is None and year is None:
        month = datetime.date.today().month
        year = datetime.date.today().year
    elif month is not None and year is None:
        year = datetime.date.today().year

    dt = datetime.date(year, month, 1)

    if month == 12:
        last_day = 31
    else:
        last_day = (datetime.date(year, month+1, 1) - datetime.timedelta(days=1)).day

    day_of_week = dt.weekday()

    for day in range(1, last_day+1):
        day_str = "%02d" % day
        if day == 1:
            if day_of_week == 0:
                cal += day_str
            else:
                cal += "% *s" % (3*day_of_week+2, day_str)
        else:
            cal += day_str

        if day_of_week == 6:
            cal += "\n"
            day_of_week = 0
        elif day_of_week != 6 and day != last_day:
            cal += " "
            day_of_week += 1

    return cal


print create_calendar_page(2, 2004)