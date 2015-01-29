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
         
print isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's'])         

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
       
print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])

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
    
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)