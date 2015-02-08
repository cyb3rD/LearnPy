#QUIZ 1 Coding Tasks
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    guessPow = 0
    if x == 1:
        return 0
    else:
        while (b**guessPow) <= x:
            guessPow += 1
        return guessPow-1
    
    
print myLog(16,2)
print myLog(15,3)

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #PLACE A LINE OF CODE HERE
        if s2 == '':
            #PLACE A LINE OF CODE HERE
        else:
            #PLACE A LINE OF CODE HERE
    return helpLaceStrings(s1, s2, '')
