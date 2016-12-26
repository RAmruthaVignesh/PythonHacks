#Write a function using recursion to check if a number n is prime (you have to check whether n is divisible by any number below n).

def recprime(num,n):
    if n<=1:
        return ""
    elif n==2:
        return "It is a prime number"
    elif num%(n-1) !=0 :
        return recprime(num,n-1)
    else:
        return "It is not a prime number"

print recprime(27,27)
