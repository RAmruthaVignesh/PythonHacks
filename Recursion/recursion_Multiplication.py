#The function takes in 2 positive numbers and multiplies them through recursive addition
def recmult(a,b):
    if a ==1: #Deal with input =1
        return b
    elif a == 0: #Deal with input = 0
        return 0
    else:
        return b + recmult(a-1 , b)

print recmult(5,10)
