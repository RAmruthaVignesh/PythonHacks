# def to check if the alphabet is a vowel
def checking_vowel(x):
    x= x.lower()
    if x == 'a' or x== 'e' or x=='i' or x=='o' or x=='u':
        return True
    else:
        return False


def only_vowels(phrase):
    #Get the sentence and check for vowel
    letter_count =0
    vowel_string = ''
    #remove the whitespaces
    phrase = phrase.replace(' ', '')
    for letter in phrase:
        letter_count= letter_count+1
        if checking_vowel(letter):
            print ("The letter number",letter_count, letter ,"is a vowel")
            # If it's a vowel, we append the letter to the vowel string
            vowel_string = vowel_string+letter
    return vowel_string

#Testcases
print only_vowels("Hello ! This is Amrutha")





