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
    #maskedString = ''
    for letter in lettersGuessed:
        countSymbols = secretWord.count(letter)
        
        #We found symbols
        if countSymbols >= 1: #How much?
            print 'Symbol: ' + str(letter) + ' founded ' + str(countSymbols)+ ' times!'
            #Only 1
            if countSymbols == 1: # just 1 symbol
                foundPos = secretWord.find(letter)
                print 'Symbol: ' + str(letter) + ' index is: [' + str(foundPos) + ']'
                #maskedString[foundPos] = letter
            # > 1
            else:
                foundPos = secretWord.find(letter)
                print 'Here we will find all positions for symbol: ' + str(letter)
                #Search all indexes of founded symbol
                while countSymbols > 0:
                    print foundPos
                    foundPos = secretWord.find(letter,foundPos+1,len(secretWord))
                    countSymbols -= 1
                    #maskedString[foundPos] = letter
        #Symbol NOT FOUNDED
        else:
            print 'Symbol: ' + str(letter) + ' NOT FOUNDED!'
            #maskedString[foundPos] = '_'
            
        #print maskedString
       
secretWord = 'aaeelpe' 
lettersGuessed = ['e', 'i', 'a', 'p', 'r', 's']    
print getGuessedWord(secretWord, lettersGuessed)