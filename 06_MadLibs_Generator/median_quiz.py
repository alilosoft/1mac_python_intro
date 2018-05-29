# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def biggest(a, b, c):
    return bigger(a, bigger(b, c))

def median(a, b, c):
    if a > b:
        if a > c:
            return bigger(b, c)
        else: # c >= a > b
            return a
    else: # a <= b
        if a > c: # c < a <= b
            return a
        else: # a <= b, c
            if b > c: # a <= c < b
                return c
            else: # a <= b <= c
                return b

def median(a, b, c):
    big = biggest(a, b, c)
    if a == big:
        return bigger(b, c)
    if b == big:
        return bigger(a, c)
    else:
        return bigger(a, b)

print median(1, 2, 3)

print median(9, 3, 6)

print median(7, 8, 7)
