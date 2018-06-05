# Algorithm: pseudo code
# days = # of days in month1 - day1
# month1 += 1
# while month1 < month2:
#     days += # of days in month1
#     month1 += 1
# days += day2
# while year1 < year2:
#     days += days in year1
#
# The above algorithm is relatively complex and  doesn't handle some special cases
#   => we need to find simpler solution, instead of trying handle all special cases.


# Simpler (Brain dead) Algorithm: the idea of the next algorithm is very simple, and very mechanical,
# it' goes through the tow dates day by day and calculate the nbr of days.
#
# days = 0
# while date1 is before date2:
#     date1 = day after date1 (nextDay(date1))
#     days += 1
# return days
# ##

