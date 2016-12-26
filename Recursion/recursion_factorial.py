#factorial ,n! = n*(n-1)!

def factorial(n):
    if (n<0):
        return "Invalid Input"
    elif(n==0):
        return 1
    else:
        return n*factorial(n-1)

def get_input():
    n = input("Enter the number to calculate factorial")
    print factorial(n)

get_input()

