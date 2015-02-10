def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
  
    
def iterPower(base, exp):
    '''
    exp: int >= 0
    returns: int or float, base^exp    base: int or float.
    '''
    result = 1
    while exp > 0:
        result *= base
        exp = exp -1
    return result 
    
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue  = min(a,b)
    if testValue == 1 :
        return b     
    
    while testValue > 1:
        if ((a % testValue) or (b % testValue)) == 0:
            return testValue
        else:
            testValue -=1
    
    return testValue
    
    # Grade Answer 
    #testValue = min(a, b)
    #
    # Keep looping until testValue divides both a & b evenly
    #while a % testValue != 0 or b % testValue != 0:
    #    testValue -= 1
    #
    #return testValue

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)   

#L5 Problem 8    
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # BASE Case: Symbol founded
    if char > aStr[len(aStr)-1]:
        return False
    # heck 1st, middle, last
    if ( (char == aStr[0]) or (char == aStr[len(aStr)-1]) or (char == aStr[(len(aStr)/2)-1]) ):
        return True
    else:
        if char < aStr[len(aStr)/2]:
            # compare with middle symbol of the 1st part
            isIn(char,aStr[0:len(aStr)/2])
        else:
            # compare with middle symbol of the second part
            isIn(char,aStr[len(aStr)/2:])
    # NOT founded            
    return False
print "Test cases for isIn(char, aStr) recurcsive:"
print 'Case: isIn(\'a\',\'abcdef\')' + 'Result: ' + str(isIn('a','abcdef'))
print 'Case: isIn(\'c\',\'abcdef\')' + 'Result: ' + str(isIn('c','abcdef'))
print 'Case: isIn(\'f\',\'abcdef\')' + 'Result: ' + str(isIn('f','abcdef'))
print 'Case: isIn(\'h\',\'abcdef\')' + 'Result: ' + str(isIn('h','abcdef'))

#L5 Problem 9
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    str1Pos = 0
    str2Pos = len(str2)-1
    # check for single-length, equal strings, length of strings
    if (len(str1) != len(str2)):
        return False
    # check if two strings are palindromes
    else:
        if str1[str1Pos] != str2[str2Pos]:
            #return False
            isPalindrome = False
            #break
        else:
        #if str1[0:str1Pos] == str2[str2Pos:]:
            str1Pos += 1
            str2Pos -= 1
            semordnilapWrapper(str1[str1Pos:], str2[0:str2Pos+1])
            
            
print  semordnilap('live', 'evil')  
print  semordnilap('lives', 'evil') 
print  semordnilap('liv', 'evil')
print  semordnilap('love', 'evil')
            
            