list = ['a', 'b', 'c', 1, 2, 3]
#print list.index('b')
#print list.index(2)
#print list.index(4)

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(li, it):
    if it in li:
        return li.index(it)
    else:
        return -1




print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1