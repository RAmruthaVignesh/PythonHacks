def coinflip(n):
    '''This function takes the input of number of coins tossed and
    gives the output of all the possible results of the toss
    '''
    flip = ['h' , 't'] #output of 1 coss toss
    if n>0: #checks if the input is valid
        print "Total number of coins is" , n
        print "Total possible output is", pow(2,n)
        coinscount = 2
        temp=[]
        result=flip
        while coinscount<=n:
            j=0
            count = pow(2,coinscount-1) 
            while j<count:
                for i in range(0,2):
                    x=result[j]+flip[i]
                    temp.append(x)
                    i=i+1
                j=j+1
            result=temp
            temp=[]                                           
            coinscount=coinscount+1
        print result
    else:
        print "invalid input"


coinflip(4)