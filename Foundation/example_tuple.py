# Tuples are immutable and defined by parentheses
new_tuple = (5,6,7,8)
print "new_tuple is:", new_tuple

# We can index them, just like strings
print "new_tuple[2] is:", new_tuple[2]

#and iterate through indicies
for index in new_tuple:
    print index

#they are immutable, we cannot redefine
#so We do something called _tuple unpacking_
(a, b, c, d) = new_tuple
print "a is:", a
print "b is:", b
print "c is:", c
print "d is:", d

# Redefine b
b=77

# Repack the tuple
new_tuple=(a,b,c,d)
print "new_tuple now is:",new_tuple
