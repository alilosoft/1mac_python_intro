# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    """
    if (year is not divisible by 4) then (it is a common year)
    else if (year is not divisible by 100) then (it is a leap year)
    else if (year is not divisible by 400) then (it is a common year)
    else (it is a leap year)
    """
    if year % 4 != 0:
        return False

    if year % 100 != 0:
        return True

    if year % 400 != 0:
        return False

    return True


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    if y1 < y2:
        while y1 < y2: # ex: 2016 -> 2018
            if isLeapYear(y1):
                days += 366
            else:
                days += 365
            y1 += 1

    if m1 < m2:
        while m1 < m2:  # ex: 01/2016 -> 05/2018
            days += daysOfMonths[m1 - 1]
            m1 += 1
    else:  # ex: 07/2016 -> 05/2018
        while m1 > m2:
            days -= daysOfMonths[m2 - 1]
            m2 += 1

    if d1 < d2:
        days += d2 - d1
    else:
        days -= d1 - d2

    return days

print daysBetweenDates(2012, 6, 29, 2013, 6, 29)
