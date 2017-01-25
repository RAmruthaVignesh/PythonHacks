
# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
import re
from MITcourse_hangman_graphic import *


WORDLIST_FILENAME = "MITcourse_HangmanWords.txt"
#WORDLIST_FILENAME = 'sample_wordlist.txt'

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()

# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    
    if ''.join(letters_guessed)== secret_word:
        return True
    else:
        return False


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    print "Guess the word" , letters_guessed

def play_hangman():
    '''This function plays the actual game'''
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. 
    secret_word  = get_word()

    #Initialize the letter guessed list
    letters_guessed = ['_' for x in range(len(secret_word))]
        #letters_guessed.append('_')
    print_guessed()

    #Checks if the word is already guessed and sets the word_status acoordingly
    win_status =  word_guessed()

    #Gets the letter input from the user and plays te game
    while win_status == False and mistakes_made<MAX_GUESSES:
        #Getting the letter input
        input_letter = raw_input("Enter the letter to be guessed : ")
        #Gets the position of the input letter from the secret_word
        if input_letter in  secret_word:
            pos = [p for p in range(len(letters_guessed)) if secret_word[p] == input_letter]
            for i in range(len(pos)):
                letters_guessed[pos[i]] = input_letter
            #Checks if the word is guessed correctly
            win_status =  word_guessed()
            print_guessed()
        else:
            mistakes_made += 1
            print_hangman_image(mistakes_made)
            print_guessed()
    else:
        print "The word to be guessed is" , secret_word

    if win_status:
        print "Congrats ! u have won!"

    return True

play_hangman()