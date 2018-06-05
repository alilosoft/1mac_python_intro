# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def isBefore(y1, m1, d1, y2, m2, d2):
    """
    Return True if the date y1, m1, d1 is before y2, m2, d2, otherwise return False
    """
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return True
        if m1 == m2:
            return d1 < d2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    while isBefore(year1, month1, day1, year2, month2, day2):
        days += 1
        year1, month1, day1 = nextDay(year1, month1, day1)
    return days


def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


def test_isBefore():
    test_cases = [((2012, 9, 29, 2012, 9, 30), True),
                  ((2012, 9, 30, 2012, 10, 30), True),
                  ((2012, 1, 1, 2013, 1, 1), True),
                  ((2012, 9, 2, 2012, 9, 1), False),
                  ((2012, 10, 1, 2012, 9, 1), False),
                  ((2013, 10, 1, 2012, 10, 1), False)]

    for (args, answer) in test_cases:
        result = isBefore(*args)
        if result != answer:
            print "Test isBefore() with data:", args, "failed"
        else:
            print "Test isBefore() passed!"


test_isBefore()
test()
