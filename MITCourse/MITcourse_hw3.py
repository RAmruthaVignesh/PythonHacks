print "**********  Exercise 3.1 ********** "
from collections import Counter
import re

def get_intersection(input_list,n):
    '''This function takes a list input and provides the values that occurs n times in the list'''
    x=Counter(input_list) # This counts the number of occurances of each unique value
    output = x.keys()[x.values().index(n-1)]
    return output

def list_intersection(*args):
    '''This function takes the input of any number of lists and finds the intersection of them'''
    base_list = args[0]
    size = len(args)
    for n in base_list:
        duplicate_list= [n for i in range(1,len(args)) if n in args[i]]
    intersection = get_intersection(duplicate_list,size)
    return intersection

# Test Cases for Exercise 3.1
intersection = list_intersection(['a','b','c','d',1,3] , [1,2,3] , ['b', 'c',3] , [2,3,4])
print  "The intersection of all the inputs is:" , intersection


print "**********  Exercise 3.2 **********"

# Define your function here
def ball_collide(ball1, ball2):
    '''This function takes in the (x,y ,radius) of 2 balls and determines if they collide'''
    #Get the radius of 2 balls
    r1 = ball1[2]
    r2 = ball2[2]
    #Get the positions of 2 balls
    x1 = ball1[0]
    x2=ball2[0]
    y1 = ball1[1]
    y2 = ball2[1]
    #Distance between the center of 2 balls when the edges touch each other
    r = (r1+r2)**2
    #Distance between the actual centers of the two balls
    ball_dist = ((x2-x1)**2) + ((y2-y1)**2)
    #The ball collides if ball_dist <= r
    if ball_dist > r :
        return False
    else:
        return True

# Test Cases for Exercise 3.2
print "Does the balls (0, 0, 1), (3, 3, 1) collide ? " , ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print "Does the balls (5, 5, 2), (2, 8, 3) collide?", ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print "Does the balls (7, 8, 2), (4, 4, 3) collide ?",ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

print "**********  Exercise 3.3 **********"

# Define your dictionary here - populate with classes from last term
my_classes = {}

def add_class(class_num, desc):
    '''This function takes 2 arguments - a class number and a description - that adds new classes
    to the dictionary my_classes'''
    global my_classes
    my_classes[class_num] = desc

def print_classes(course):
    '''This function that takes one argument and prints out all the classes in that Course'''
    global my_classes
    for key , value in my_classes.iteritems():
        if key.startswith(course):
            print key ,my_classes[key]

# Test Cases for Exercise 3.3
# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')
add_class('6.2', 'Advanced Python')
add_class('7', 'Deep Learning')
print "The classes under course 6 are :",print_classes('6')

print "**********  Exercise 3.4 **********"

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    '''This function combines 2 lists into a dict'''
    comb_dict = {}
    comb_dict = dict(zip(l1,l2))
    return comb_dict

combined_dict = combine_lists(NAMES , AGES) 

def people(age):
    '''This function takes in an age and returns the names of all the people who are that age.'''
    global combined_dict
    people_subset = [key for key,value in combined_dict.iteritems() if value == age]
    return people_subset

# Test Cases for Exercise 3.4 
print "The list of all the people with age 20 are :" , people(20)
print "The list of all the people with age 21 are :" ,people(21)# ==   ['Bob']
print "The list of all the people with age 22 are :",people(22) #==   ['Kelly']
print "The list of all the people with age 23 are :",people(23)#==   []

print "**********  Exercise 3.5 **********"

month_list = ['March', 'April','May','June','July','August','September' ,'October ','November' ,'December' ,'January','February']
month_values= range(1,13)
month_dict=dict(zip(month_list,month_values))
Day = {0:'Sunday' , 1:'Monday' , 2:'Tuesday', 3:'Wednesday' , 4:'Thursday' , 5:'Friday' , 6:'Saturday'}

def zellers(month, day, year):
    '''This function takes in the input of month ,date and year and computes the day of the week on which a given date will fall (or fell)'''
    global month_dict
    global Day
    A=month_dict[month]
    B=day
    C=year%100
    D=year/100

    # -- W = (13*A - 1) / 5
    # -- X = C / 4
    # -- Y = D / 4
    # -- Z = W + X + Y + B + C - 2*D
    # --R = the remainder when Z is divided by 7
    W = (13*A - 1) / 5
    X = C / 4
    Y = D / 4
    Z = W + X + Y + B + C - 2*D
    R = Z%7
    while R<0:
        R=R+7

    return Day[R]

# Test Cases for Exercise 3.5
print "The entered date falls on", zellers('March', 10, 1940)# == "Sunday" # This should be True