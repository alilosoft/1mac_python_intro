s = 'Hello'
# s[0] = 'Y' # not allowed because strings are immutable

p = ['H', 'e', 'l', 'l', 'o']
print p
p[0] = 'Y'
print p
q = p
q[0] = 'H'
print p, q
