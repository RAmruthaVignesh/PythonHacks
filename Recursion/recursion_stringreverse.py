#Write a function using recursion that takes in a string and returns a reversed copy of the string. The only string operation you are allowed to use is string concatenation.

def recstringreverse(stringip,length):
    if length ==0:
        return "\nReversal done"
    else:
        return stringip[length-1]+recstringreverse(stringip,length-1)

print recstringreverse("Amrutha",len("Amrutha"))