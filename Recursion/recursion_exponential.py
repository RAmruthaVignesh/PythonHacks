def recexp(b,e):
    if (e<0):
        return "Invalid Input"
    elif(e==0):
        return 1
    else:
        return b*recexp(b,e-1)

print recexp(2,5)