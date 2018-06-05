# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def isLeapYear(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

def daysInMonth(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    return days_in_month[month - 1]

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    assert daysBetweenDates(2012, 1, 1, 2012, 2, 28) == 58
    assert daysBetweenDates(2012, 1, 1, 2012, 3, 1) == 60
    assert daysBetweenDates(2011, 6, 30, 2012, 6, 30) == 366
    assert daysBetweenDates(2011, 1, 1, 2012, 8, 8) == 585
    assert daysBetweenDates(1900, 1, 1, 1999, 12, 31) == 36523

    assert nextDay(1999, 1, 1) == (1999, 1, 2)
    assert nextDay(1999, 12, 31) == (2000, 1, 1)
    assert nextDay(1999, 2, 28) == (1999, 3, 1)
    assert nextDay(2000, 2, 28) == (2000, 2, 29)

    print "test() finish"

test()

def test_nextDay_using_stub():
    test_cases = [((2012, 1, 1), (2012, 1, 2)),
                  ((2012, 1, 30), (2012, 2, 1)),
                  ((2012, 12, 30), (2013, 1, 1))]

    for (date, next_day) in test_cases:
        actual = nextDay(*date)
        assert actual == next_day
        if actual != next_day:
            print "Test failed with ", date
        else:
            print "Test nextDay() passed"

# test_nextDay_using_stub()

def test_daysInMonth_no_leap():
    test_cases = [(1, 31), (2, 28),
                  (3, 31), (4, 30)]
    for (month, expected) in test_cases:
        actual = daysInMonth(1999, month)
        assert expected == actual
        if expected == actual:
            print "test daysInMonth() passed"
        else:
            print "test daysInMonth() failed"

test_daysInMonth_no_leap()

def test_daysInMonth_with_leap():
    test_cases = [((1840, 2), 29), ((2000, 2), 29),
                  ((2001, 2), 28), ((1983, 2), 28)]
    for (month, expected) in test_cases:
        actual = daysInMonth(*month)
        assert expected == actual
        if expected == actual:
            print "test daysInMonth() passed"
        else:
            print "test daysInMonth({}) failed".format(month)

test_daysInMonth_with_leap()

def test_isLeapYear():
    test_cases = [(1804, True),
                  (1840, True),
                  (2000, True),
                  (2001, False),
                  (2296, True)]
    for (year, is_leap) in test_cases:
        actual = isLeapYear(year)
        # print year, is_leap, actual
        assert actual == is_leap
        if actual == is_leap:
            print "isLeap() test passed"
        else:
            print "isLeap({}) failed".format(year)

test_isLeapYear()

