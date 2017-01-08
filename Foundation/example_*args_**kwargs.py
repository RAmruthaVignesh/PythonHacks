#When the number of arguments is unknown while defining the functions *args and **kwargs are used
import numpy as np

def mean_of_numbers(*args):
    '''This function takes any number of numerical inputs and returns the mean'''
    args = np.array(args)
    mean = np.mean(args)
    return mean

print "The mean of the numbers :" , mean_of_numbers(2,3,4.1,5,8)

def string_concat(*args,**kwargs):
    '''This function takes any number of arguments and keyword arguments. 
    Converts into string and concatenates them'''
    string_input_args= [str(i) for i in args]
    args_out = ''.join(string_input_args)
    input_kwargs = [kwargs[j] for j in kwargs]
    kwargs_out = ''.join(input_kwargs)
    return args_out+kwargs_out

string_out= string_concat(1,2, a="Hi" , b= "howdy?" )
print "The concatenated string output are " , string_out






