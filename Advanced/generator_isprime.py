def isprime(x):
    '''This function takes in a number and returns boolean value of if it is prime or not'''
    if x%2 != 0: # checks if it is odd
        if x==1: # if it is 1 , return not prime
            return False
        else:# if odd and greater than 3
            for i in range(3,x,2):#check if its prime
                if x%i ==0:
                    return False       
            return True
    else:
        if x==2:#If it is 2 ,return true , else return not prime
            return True
        else :
            return False


def primerange(to ,fro=1):
    '''This function takes to and from values and returns a generator function that provides the prime numbers in that range'''
    for i in range(fro ,to+1):
        if isprime(i):
            yield i
        i=i+1

#Testcases
gen_prime = primerange(100 , fro =50)
primes= [next(gen_prime) for i in range(3)]
print "First 3 prime numbers between 50 and 100 are " , primes




