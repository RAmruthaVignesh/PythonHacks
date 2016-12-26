#Write a recursive function that takes in one argument n and computes Fn, the nth value of the Fibonacci sequence. Recall that the Fibonacci sequence is defined by the relation 


def recfibonacci(n):
    if  n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recfibonacci(n-1)+ recfibonacci(n-2)

print recfibonacci(10)