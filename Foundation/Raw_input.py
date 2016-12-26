# Raw_input is similar to scanf of C

name = raw_input("what is your name?")
city = raw_input("which city are you from?")

# The greetings can be printed using the variables set with raw_input
print("Hello there ! It is great to meet you")
print name , "from" , city

#raw_input returns string and hence cannot be used for mathematical calculations
#input can be used for mathematical calculations too!

age = input("how old are you?")
print "wow ! you look like" ,  0.60*age , "only"

#int(argument) rounds up the value
print "wow ! you look like" ,  int(0.60*age) , "only"

