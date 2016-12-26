##### Template for Homework 2, exercises 2.0 - 2.5  ######
import math
import random
# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
def is_divisible(m,n):
    """ This function takes 2 inputs m ,n
    It checks if m is divisible by n.
    And returns True or False."""
    if n!=0:
        if (m%n ==0):
            return True
        else:
            return False
    else:
        return "Invalid Input"


# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function
print "********* Test cases for is_divisible ********"
print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
def not_equal(m,n):
    """ This function takes 2 inputs m and n and checks if m is not qual to n"""
    if (m==n):
        return True
    else:
        return False

# Test cases for not_equal
print "******** Test cases for not_equal **********"
print not_equal(10,5) # This should return False
print not_equal(0,0) # This should return True
print not_equal('Amrutha' , 'Amrutha') #This should return True

# ********** Exercise 2.3 ********** 

## 1 - multadd function
"""This function takes 3 inputs a , b ,c and computes a*b+c"""
def multadd(a,b,c):
    return a*b+c
print "********** Test cases for multadd ***********"
print multadd(6,3,3), 6*3+3
print multadd(1,0,9), 1*0+9
print multadd(-1,0,-9), -1*0-9
print multadd(-1,30,-9), -1*30-9

## 2 - Equations
print "angle_test : sin(pi/4) + cos(pi/4)/2 is" , multadd(1,math.sin(math.pi /4),math.cos(math.pi/4)/2)
print "ceiling_test : ceiling(276/19) + 2 log_7(12) is" , multadd(1,math.ceil(276.0/19.0), 2*math.log(12,7))

## 3 - yikes function
def yikes(x):
    """This function takes 1 input and returns yikes output"""
    ex = math.pow(math.e , -x)
    return multadd(x,ex, math.sqrt(1- ex))

print "********* yikes function************"
# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    """ This function takes no paramater and generates a random number .
    It checks if the random number is divisible by 3 .
    Returns True or False accordingly"""
    x=random.randint(0 , 1000)
    print "The generated random number is" , x
    if x%3 ==0:
        return True
    else:
        return False

# Test Cases
print "******* Test cases for rand_divis_3 ********"
print rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
def roll_dice(sides , dice):
    """ This function takes the  2 inputs ,
    sides - number of sides of each dice
    dice - number of dices
    and gives out the random roll values of each dice."""
    x=1
    while (x<=dice):
        print random.randint(1,sides)
        x=x+1
    else:
        print "That's all.."
# Test Cases
print "*******Testcases for roll_dice ********"
roll_dice(6,10)
# ********** Exercise 2.5 **********

# code for roots function
def roots(a,b,c):
    """This fuction takes in 3 inputs,the discriminants of the quadratic equation.
    It returns the roots of the quadratic equation"""
    x = (b*b)-(4*a*c)
    if x<0: # If this condition is true , complex roots are returned
        y=math.sqrt(-x)
        root1 = complex(-b,y)/(2*a)
        root2 = complex(-b,-y)/(2*a)
        roots=[root1 , root2]
        return roots
    else:# This returns the real number roots of the quadratic equation
        y=math.sqrt(x)
        root1 = (-b + y)/(2*a)
        root2 = (-b - y)/(2*a)
        roots=[root1 , root2]
        return roots

# Test Cases
print "****** Test cases for roots- roots of the quadratic equation*********"
print "The roots of x^2-3x-4 is ", roots(1,-3,-4) # should return -1 and 4
print "The roots of 6x^2+11x-35 is ",roots(6,11,-35)# should return -3.5 and 1.66
print "The roots of x^2-7x is ",roots(1,-7,0)#should return 7 and 0
print "The roots of x^2+2x+10 is ",roots(1,2,10)#should return (-1+3j) and (-1-3j)
print "The roots of x^2-4x+7 is " ,roots(1,-4,7)#should retun (2+sqrt(3)) and (2-sqrt(3))