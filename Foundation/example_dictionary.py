#Example of simple dictionary
sample_dict = {'Name':'zara' , 'age':8 , 'class' : 'first'}
print "sample_dict['Name']:",sample_dict['Name']
#If we attempt to access a data item with a key, which is not part of the dictionary, we get an error

#To update the dictionary
sample_dict['age'] = 8
print "sample_dict['age'] :",sample_dict['age']
#To add a new key-value pair to the dictionary
sample_dict['school'] = 'DAV'
print "The sample dict is" , sample_dict

#To delete dictionary elements
del sample_dict['school']
print "The sample dict is" , sample_dict
#To remove all the entries of the dict
sample_dict.clear()
print "The sample dict is" , sample_dict
#To delete the dict
del sample_dict

#More than 1 entry per key is not allowed. In case of duplication , the last assignment wins
sample_dict = {'name':'zara' , 'age':8 , 'name':'swetha'}
print "The sample dict is:" , sample_dict

