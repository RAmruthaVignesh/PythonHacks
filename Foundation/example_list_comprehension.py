#Example 1 : To make a list of letters in the string
print  "This example makes a list of letters in a string"
print [letter for letter in "hello , _world!"]

#Example 2: Add an exclamation point to every letter
print "\nExample 2: Add an exclamation point to every letter"
print [letter+"!" for letter in "hello , world !"]

#Example 3 : To generate multiplication table of 9
print "\nExample 3: A multiplication table for the 9's"
print [num*9 for num in range(1,13)]

#Example 4 : To print letters if they are not o
print "\nExample 4: Make a list of letters in a string if they're not 'o'"
print [letter for letter in "hello_world" if letter!="o"]