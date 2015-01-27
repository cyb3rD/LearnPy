def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
   
    return min(max(lo,x), hi)
    
print clip(3,4,5) #must be 4
print clip(3,1,5) #must be 3
print clip(3,6,5) #must be 5