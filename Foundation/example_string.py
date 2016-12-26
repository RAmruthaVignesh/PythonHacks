# Define a string
sample_string = 'Hi there!'

#We can concatenate two strings together with + sign
print "your 1st example string is " + sample_string
#Another example
s1 = "This is"
s2 = 'Amrutha'
print "your 2nd example string is " + s1 + s2
# but remember, gluing together with a comma adds an extra space
print "Remember, gluing together with a comma adds an extra space!" , s1, s2

# Remember we can iterate through it
print "Remember we can iterate through it!"
for letter in sample_string:
    print letter

#We can also index the string
print "We can also index the string"
print  "sample_string[0] is",sample_string[0]
#and slice it
print "sample_string[3:8] is" , sample_string[3:8]

#We can get the length of our string using the len function
print "len(sample string) is" , len(sample_string)

# And use various string methods on it
print "sample_string.upper()", sample_string.upper()
print "sample_string.lower()", sample_string.lower()
