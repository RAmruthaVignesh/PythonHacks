#Start your program by asking the user for a phrase to encode and the shiftvalue
phrase = raw_input("Enter the phrase to be encoded")
shift_value = input("Please enter the shift value")
encoded_phrase = ''

for c in phrase:
    encoded_phrase = encoded_phrase + c
print "This loop prints the phrase as it is !" ,encoded_phrase

#Now modify the program above to replace all the alphabetic characters with x.
phrase = raw_input("Enter the phrase to be encoded")
shift_value = input("Please enter the shift value")
encoded_phrase = ''

for c in phrase:
    if c.isalpha(): #Checks if the input is an alphabet
        if c.isupper(): #checks if the input is uppercase
            encoded_phrase = encoded_phrase + 'X'
        else:
            encoded_phrase = encoded_phrase + 'x'
    else:
        encoded_phrase = encoded_phrase + c
print "This loop changes the alphabets alone to X" ,encoded_phrase

#Now modify your code so that it produces the encoded string using the cyclic cipher with the shift value entered by the user
""" This piece of code takes in the input string and the shift value .
It shifts the alphabets by the shift value. The shifting is taken care for upper case and lower case seperately """
phrase = raw_input("Enter the phrase to be encoded")
shift_value = input("Please enter the shift value")
encoded_phrase = ''
for c in phrase:
    if c.isalpha(): #Checks if the input is an alphabet
        if c.isupper(): #checks if the input is uppercase
            c = ord(c)-ord('A')
            encoded_phrase = encoded_phrase + chr(((c+shift_value)%26)+ord('A'))
        else:
            c = ord(c)-ord('a')
            encoded_phrase = encoded_phrase + chr(((c+shift_value)%26)+ord('a'))
    else:
        encoded_phrase = encoded_phrase + c
print "This is the secret message ! Shhhh.." ,encoded_phrase