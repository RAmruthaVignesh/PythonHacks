#The 'else' of the 'while/else' will be executed if the 'while' loop is exited normally

n =  input("enter a positive number")
while (n>=0):
    print n
    n=n-1
else:
    print "The number is no more positive"