if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20:
    print "Did you know that 10 is greater than 20!?" # never executed
else:
    print "Of course, 20 is greater than 10"


def absolute(a):
    if a < 0:
        return -a
    return a

print absolute(5), absolute(-5)

def bigger(a, b):
    if a > b :
        return a
    return b

print bigger(1, 2), bigger(2, 1)

def biggest(a, b, c):
    if a > b:
        if a > c:
            return a
        else: # a <= c
            return c
    else: # a <= b
        if b > c:
            return b
        else: # b <= c
            return c

print biggest(9, 6, 3)
print biggest(6, 9, 3)
print biggest(6, 3, 9)

def biggest(a, b, c):
    if a > b:
        return bigger(a, c)
    else: # a <= b
        return bigger(b, c)

print biggest(9, 6, 3)
print biggest(6, 9, 3)
print biggest(6, 3, 9)

def biggest(a, b, c):
    return bigger(a, bigger(b, c))

print biggest(9, 6, 3)
print biggest(6, 9, 3)
print biggest(6, 3, 9)

def biggest(a, b, c):
    return max(a, b, c)
