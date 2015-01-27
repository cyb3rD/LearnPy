#sample function
def f(x):
    import math
    return  400*math.e**(math.log(0.5)/3.66 * x)
    
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    numOfSteps = (stop-start)/step
    print "Num of steps: " + str(numOfSteps)
    initStep = 0
    current = start
    exposure = 0
    while (initStep <= numOfSteps):
        exposure += f(current)
        print 'Step: '+str(initStep)+'| x = '+str(current)+' F(x):'+str(f(current))+' Exp = '+str(exposure)
        #count += 1
        current += step
        initStep += 1
    return exposure
    
#print radiationExposure(0, 5, 1)
#print radiationExposure(5, 11, 1)
#print radiationExposure(0, 11, 1)
print radiationExposure(0, 4, 0.25)