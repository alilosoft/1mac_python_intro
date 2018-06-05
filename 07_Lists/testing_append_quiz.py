p =[1,2]
q = [3,4]
p.append(q) # append a reference to q at the end of p
print p, len(p)
q.append(5)
print p, len(p)