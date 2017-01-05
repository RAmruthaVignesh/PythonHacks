from collections import OrderedDict

#The zip function zips the two tuples into list of tuples
A0 = zip(('a','b','c','d','e'),(1,2,3,4,5))
print "The output of zip of two tuples of equal length is :" , A0
#The dict function here creates a dict out of the tuple
A0 = dict(A0)
print "The dict of A0 is : " , dict(A0)
print "*****************************************************************"

#The range function prints the list of low to high-1
A1 = range(10)
print "The output of range(10) is : ",A1
print "*****************************************************************"

#This is the list comprehension , it prints a list of all values in A1 if the value is present in the keys of A0
A2 = [i for i in A1 if i in A0]
print "The list comprehension that prints the values of A1 that are present in A0 : " , A2
print "Note that the list is empty because it checks if A1 is present in the keys of A0: "
A2new = [i for i in A1 if i in A0.values()]
print "The list comprehension that prints the values of A1 that are present in A0.values() : ",A2new
print "*****************************************************************"

#The is the list comprehension , it loops through every key in A0 and prints its values
A3 = [A0[s] for s in A0]
print "This list comprehension loops through every key in A0 and prints A0[key] : " , A3
print "Not that the values are not in order. The dict does not save in order , we will have to use OrderedDict to solve this"
print "*****************************************************************"

#List comprehension 
A4 = [i for i in A1 if i in A3]
print "List comprehension that prints A1 if the value is available in A3 : " ,A4
print "*****************************************************************"

#Dictionary of A1 and its square
A5 = {i:i*i for i in A1}
print "The dictionary of A1 as keys and its square as values :" ,A5
print "*****************************************************************"

#List of lists
A6 = [[i,i*i] for i in A1]
print "List of list of A1 and its square : " , A6
print "*****************************************************************"

