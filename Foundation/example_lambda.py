import math
# Lambda functions are anonymous functions

#To find the square root of a function
sqroot = lambda x : math.sqrt(x)
print "The square root as calculated by the lambda function is : " ,sqroot(4)

#To find the sum of 2 numbers
sum = lambda x,y : x+y
print "The sum as calculated by the lambda function is : " ,sum(4,6)

# A function that returns lambda function that increments value
def make_increment(n):
    return lambda x:x+n

increment_by_2 = make_increment(2)
print "To increment by 2 using lambda function: " , increment_by_2(10)
