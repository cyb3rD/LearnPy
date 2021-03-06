# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "d:\GitHub\LearnPy\words.txt"

def loadWords():
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
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    countFind = 0
    for letterSecret in secretWord:
        for letterGuess in lettersGuessed:
            if letterSecret == letterGuess:
                countFind +=1
    if countFind < len(secretWord):
         return False
    else:
         return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    maskedString = ''
    #convert list of symbols to string
    strLettersGuessed = ''.join(lettersGuessed)
    
    for letter in secretWord:
        foundLetterResult = strLettersGuessed.find(letter)
        if foundLetterResult > -1:
            
            maskedString += letter
        else:
                maskedString += '_ '
    return maskedString

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string 
    alphabet = string.ascii_lowercase
    maskedString = ''
    strLettersGuessed = ''.join(lettersGuessed)
    
    for letter in alphabet:
        foundLetterResult = strLettersGuessed.find(letter)
        if foundLetterResult == -1:
            maskedString += letter
        
    return maskedString

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    import string
    lenSecretWord = len(secretWord)
    numOfGuesses = 8
    alphabet = string.ascii_lowercase
    lettersGuessed = ''
        
    print "Welcome to the game Hangman"
    print "I am thinking of a word that is " + str(lenSecretWord) + " letters long"
    
    print "-------------"
    print "You have " + str(numOfGuesses) + " guesses left."
    print "Available letters: " + alphabet
 
    #Main Cycle through numOfGuesses
    while numOfGuesses > 0 :
        userInput = raw_input("Please guess a letter: ")
        userInput = userInput.lower()
        
        # check letter in Gueessed
        if userInput in lettersGuessed:
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print  "Oops! You've already guessed that letter: " +  guessedWord
            print "-------------"
            print "You have " + str(numOfGuesses) + " guesses left"
            print "Available letters: " + getAvailableLetters(lettersGuessed)
            continue
        
        # check letter in secretWord
        if userInput in secretWord:
            lettersGuessed += userInput
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            # check for win
            if isWordGuessed(secretWord, lettersGuessed):
                print "Good guess: " + guessedWord
                print "-------------"    
                print "Congratulations, you won!"
                break
            print "Good guess: " + guessedWord
            print "-------------"
            print "You have " + str(numOfGuesses) + " guesses left"
            print "Available letters: " + getAvailableLetters(lettersGuessed)
            # nextRound
        else:
            # else Oops! Decrement numOfGuesses
            lettersGuessed += userInput
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            numOfGuesses -= 1
            print "Oops! That letter is not in my word: " + guessedWord
            print "-------------"
            # You loose!
            if numOfGuesses == 0:
                print "Sorry, you ran out of guesses. The word was " + secretWord
                break
            
            print "You have " + str(numOfGuesses) + " guesses left"
            print "Available letters: " + getAvailableLetters(lettersGuessed)
            
          
# secretWord = chooseWord(wordlist).lower()

secretWord = 'c'
hangman(secretWord)