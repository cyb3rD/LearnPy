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

print iterPower (2, 0)
print iterPower (2, 3)
