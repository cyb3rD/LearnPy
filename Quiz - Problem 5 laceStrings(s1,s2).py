# Quiz - Problem 5
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    lacedString = ''
    if s1 == '':
        lacedString = s2
        return lacedString
    if s2 == '':
        lacedString = s1
        return lacedString
        
    # S1 == S2
    if len(s1) == len(s2):
        for i in range (len(s2)):
            # Take by 1 symbol from each string
            lacedString += s1[i]+s2[i]
        return lacedString
    # S1 >S2
    if len(s1) > len(s2):
        for i in range (len(s2)):
            # Take by 1 symbol from each string
            lacedString += s1[i]+s2[i]
        lacedString += s1[i+1:]             
        return lacedString
    # S2 > S1
    else:
        for i in range (len(s1)):
            # Take by 1 symbol from each string
            lacedString += s1[i]+s2[i]
        lacedString += s2[i+1:]             
        return lacedString
        
