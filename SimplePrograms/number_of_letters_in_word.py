#get the word to be counted
word_to_count = 'hello_world!'
print ("the word is" , word_to_count)

# iniliatize the letter count
letter_count = 0

#loop through the word
for letter in word_to_count:
    print("the letter", letter, "#number" , letter_count)
    letter_count = letter_count+1

print ("there are", letter_count, " letters in", word_to_count)