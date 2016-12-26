# Lists are defined by brackets
sample_list = [1,5,10,100]

#We can concatenate two strings together with a comma
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print "Remember, gluing together with a comma adds an extra space!" , L1,L2

# Remember we can iterate through the list
print "Remember we can iterate through the list!"
for item in sample_list:
    print item

#We can also index the list
print "We can also index the list"
print  "sample_list[0] is",sample_list[0]
#and slice it
print "sample_string[1:4] is" , sample_list[1:4]

#We can get the length of our string using the len function
print "len(sample list) is" , len(sample_list)

#Lists, however, are mutable! So, if we want we can change the value of one element
sample_list[2] = 50
print "The updated list is" , sample_list

# Or, add on a new element with append:
sample_list.append(2000)
print "The appended list is" , sample_list

# Or insert
sample_list.insert(0,2) #(position , value)
print "The updated list after insertion is" , sample_list

# Or even delete an element using remove
sample_list.remove(2000)
print "The updated list after removal is" , sample_list

