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
    
    # Grade Aswer 
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
    
