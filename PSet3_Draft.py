def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    countFind = 0
    for letterSecret in secretWord:
        for letterGuess in lettersGuessed:
            if letterSecret == letterGuess:
                countFind +=1
    if countFind < len(secretWord):
         return False
    else:
         return True
         
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)         

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    foundPos = -1
    countSymbols = 0
    for letter in lettersGuessed:
        countSymbols = secretWord.count(letter)
        
        
        if countSymbols >= 1: #foundPos also > 0
            print 'Symbol: ' + str(letter) + ' founded ' + str(countSymbols)+ ' times!'
            
            if countSymbols == 1: # just 1 symbol
                foundPos = secretWord.find(letter)
                print 'Symbol: ' + str(letter) + ' index is: [' + str(foundPos) + ']'
            else:
                print 'Here we will find all positions for symbol: ' + str(letter)
                #Search all indexes of founded symbol
                while foundPos < len(secretWord):
                    print foundPos
        else:
            print 'Symbol: ' + str(letter) + ' NOT FOUNDED!'
            
       
secretWord = 'aaeelpe' 
lettersGuessed = ['e', 'i', 'a', 'p', 'r', 's']    
print getGuessedWord(secretWord, lettersGuessed)