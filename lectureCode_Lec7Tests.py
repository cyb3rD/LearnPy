def isPal(x):
    assert type(x) == list
    #temp = x
    
    temp = x[:] # Make a copy of source list
    
    # 4. Try to find wjere the bug is
    #print(temp, x)
    #temp.reverse # BUG 2 with reversion of temp
    
    temp.reverse() # Correct string
    
    # 3. Try to find wjere the bug is
    #print(temp, x)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = [] # FIXED initialisation
    for i in range(n):
        #result = [] # BUG 1 - always init with empty lis
        elem = raw_input('Enter element: ')
        result.append(elem)
        # 2. Try to find wjere the bug is
        print(result)
    if isPal(result):
        # 1. Try to find wjere the bug is
        print(result)
        print('Yes')
    else:
        print('No')
