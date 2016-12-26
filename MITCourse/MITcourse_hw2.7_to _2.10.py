
# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "****** Testcases for sum_all **********"
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers
    total = 0
    cum_sum = []
    for number in number_list:
        total = total + number
        cum_sum.append(total)
    return cum_sum

# Test cases
print "******* Testcases for cumulative sum ******"
print "cumulative_sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6])
print "cumulative_sum of [1, 2, 3, 4] is:", cumulative_sum([1, 2, 3, 4])

# **********  Exercise 2.8 **********

def report_card():
    '''
    This function takes in user inputs 
    number of classes taken, name of the subjects and their scores and then
    calculates overall GPA 
    '''
    num_classes = input("How many classes did you take?")
    init = 1
    classname = []
    classgrade= []
    while (init<= num_classes):
        name = raw_input("What was the name of this class?")
        classname.append(name)
        grade = input("What was your grade?")
        classgrade.append(grade)
        init = init+1
    init=0
    print "REPORT CARD:\n"
    while (init<num_classes):
        print init+1
        print classname[init],"-",classgrade[init]
        init=init+1
    else:
        print "overall GPA :" , sum_all(classgrade)/num_classes
# Test Cases
report_card()

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

vowels = ['a', 'e', 'i', 'o', 'u','A' , 'E' , 'I' , 'O' , 'U']
def pig_latin(word):
# word is a string to convert to pig-latin
    '''takes in a single word, then converts the word to Pig Latin. 
    Pig Latin takes the first letter of a word, puts it at the end, and appends ay. 
    If the first letter is a vowel, we keep it as it is and append hay to the end '''
    if word[0] in vowels:
        word = word+"hay"
        return word
    else:
        wordlength =  len(word)
        word = word[1:wordlength]+word[0]+"ay"
        return word

# Test Cases
print "******Test cases for Pig Latin ************"
print pig_latin("Amrutha")
print pig_latin("Vignesh")


# **********  Exercise 2.10 **********
def cube_list():
    '''prints a list of the cubes of the numbers 1 through 10'''
    print "List of cubes from 1 to 10"
    print [num*num*num for num in range(1,11)]

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

def vowels(ipstring):
    '''This function takes a string input and  prints the vowels in the string'''
    vowels = ['a', 'e', 'i', 'o', 'u','A' , 'E' , 'I' , 'O' , 'U']
    print "The vowels in the input string are "
    print  [letter for letter in ipstring if letter in vowels]


def  y(x):
    print  "list of [x,y] pairs where y= x^2+1"
    print [[x,x*x+1] for x in range(-5,5) if (x*x)+1<=10 ]


# Test Cases
print "******* Testcases for List Comprehension******"
cube_list()
print "------------------"
coinflip(2)
print "------------------"
vowels('Amrutha')


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 