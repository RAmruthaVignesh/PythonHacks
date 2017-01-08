def sort_dict_based_on_values(ipdict):
    '''This function takes the input of a dict and returns a list of keys
     sorted in the order of its values'''
    return sorted(ipdict , key = lambda i: ipdict[i])


sample_dict = {'A':35 , 'B':70, 'C':10 , 'D':100, 'E':1.25}
print "The Sample list sorted according to its values : ", sort_dict_based_on_values(sample_dict)