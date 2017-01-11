import os
import re

def printmatch(match):
    '''This function takes the input of the matched expression and 
    prints accordingly'''
    if match:
        print "The matched string is:" ,match.group()
        print "**********************"
    else:
        print "The string to match is Not found"
        print "**********************"   

def regex_basicpatterns(path):
    '''This functions gives some examples of regular expressions'''
    #open the file and load the entire text as a string
    with open(path,'rw') as str:
        lines=''.join([line.strip('\n') for line in str])

    #Match characters in the strings
    print "Example 1: To match the first pattern 'th' in the string and print it"
    match = re.search(r'th',lines)
    printmatch(match)

    #Match any single character except newline
    print "Example 2 : To match a 3 characters before and after 'th'"
    match = re.search(r'...th...', lines)
    printmatch(match)

    #Match a digit character and word character
    print "Example 3: To match the first pattern of a digit followed by 2 characters in the string and print it"
    match = re.search(r'\d\w\w',lines)
    printmatch(match)

    #Match the repetition 
    print "Example 4: To match a character and repetition of 'i' and then a character following"
    match = re.search(r'.i+.', 'piiiig')
    printmatch(match)

    #Match the whitespace char
    print "Example 5: To match zero or more whitespace character"
    match = re.search(r'\s*\d\s*..',lines)
    printmatch(match)

    #Match the start of the string
    print "Example 6 : To match the start of the line"
    match = re.search(r'^\w+', lines)
    printmatch(match)


regex_basicpatterns("../FileOperations/sampletext.txt")