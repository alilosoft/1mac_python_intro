
def sum_none(a, b):
    a+b


print sum_none(1, 2)  # A function without return statement has no output


def increment(n):
    n += 1
    return n


n = 10
print increment(n)  # parameters are passed by value
print n  # still 10


def square(x):
    return x * x


print square(5), square(square(5))  # we can use function composition like the las one
