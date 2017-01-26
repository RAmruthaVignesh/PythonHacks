from collections import Counter

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

#Testcases
intersection = list_intersection(['a','b','c','d',1,3] , [1,2,3] , ['b', 'c',3] , [2,3,4])
print  "The intersection of all the inputs is:" , intersection