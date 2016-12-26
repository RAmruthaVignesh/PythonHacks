#Write a function using recursion to print numbers from n to 0.

def recprint(n):
    if n==0:
        return 0
    elif (n<0):
        print n
        return recprint(n+1)
    else:
        print n
        return recprint(n-1)

print recprint(-10)