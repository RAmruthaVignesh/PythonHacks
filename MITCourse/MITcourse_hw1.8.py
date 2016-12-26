print "****Using a for loop, write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4, . . . , 1/10. ****"
print [1.0/number for number in  range(2,11)]

# *****************************************************************#
import math
print "***Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero***"
a= input("Enter a positive number:")
a= math.floor(a)
while(a>0):
    print a
    a=a-1

# *****************************************************************#
print "Write a program using a for loop that calculates exponentials. Your program should ask the user for a base base and an exponent exp, and calculate base**exp."
base = input("Enter the base:")
exp = input("Enter the exponent:")
result=1
for number in range(1,exp+1):
    result = base*result
print "Base ** exp =" , result

# *****************************************************************#
print "Write a program using a while loop that asks the user to enter a number that is divisible by 2."
print "Give the usera witty message if they enter something that is not divisible by 2- and make them enter a new number. "
print "Dont let them stop until they enter an even number"
print " Print a congratulatory message when they finally get it right."
x= input("Enter an even number")
xrem = x%2
while(xrem !=0):
    print ("This is not an even number ! Enter a new one")
    x= input("Enter an even number")
    xrem = x%2
else:
    print "Thanks! Got it"

