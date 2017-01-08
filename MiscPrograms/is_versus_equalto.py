#common mistakes - is versus ==
a=[1,2]
b=[1,2]
c=a
#result of is
result =a is b
print "The result of a is b is:" ,result
result =a is c
print "The result of a is c is:" ,result

#result of  ==
result = (a==b)
print "The result of a == b is:" ,result
result = (a==c)
print "The result of a == c is:" ,result