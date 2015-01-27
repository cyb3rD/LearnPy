print 'Please think of a number between 0 and 100!'
start = 0
stop = 100
guess = (start+stop)/2

help = 'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.'
sorry = 'Sorry, I did not understand your input.'
strAnswer = 'Game over. Your secret number was: '
question = 'Is your secret number '
answer = guess
isAnswered = False

while not (isAnswered):
    print question + str(guess) + '?'
    answer = raw_input(help)
   
    if (answer == 'h'):
        stop = guess
        guess = (start+stop)/2
        continue
    if (answer == 'l'):
        start = guess
        guess = (start+stop)/2
        continue
    if (answer == 'c'):
        print strAnswer + str(guess)
        isAnswered = True
        break
    
    print sorry    

    
