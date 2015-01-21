#
# Increse speed of computation fixed monthly payment by using bisectional search
#

balance = 999999 # comment beforesubmission
annualInterestRate = 0.18 # comment beforesubmission

monthlyInterestRate = annualInterestRate /12.0

month = 1
totalPaid = 0.0

initialBalance = balance #save initial balance
# init data for bisectional search
monthlyPaymentLowerBound = balance / 12.0
monthlyPaymentUpperBound =  (balance * (1 + monthlyInterestRate)**12) / 12.0

tolerance = 0.01

def getPayment(min, max):
    return (min+max)/2.0

initFixedMonthlyPayment =  getPayment(monthlyPaymentLowerBound, monthlyPaymentUpperBound)  
fixedMonthlyPayment = initFixedMonthlyPayment

previousBalance = initialBalance

while month <= 12:

    totalPaid += fixedMonthlyPayment
    
    monthlyUnpaidBalance = previousBalance - fixedMonthlyPayment

    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    previousBalance = updatedBalance
        
    if month == 12:
        #
        # Find new fixed payment (fixedMonthlyPayment)
        #
        print 'Total paid: ' + str(totalPaid)
        
        #if totalPaid > initialBalance:
            
        
        
        diffPaid = totalPaid - initialBalance
        print 'diff: ' + str(diffPaid)
        if (diffPaid <= tolerance):
            print 'Payment: ' + str(fixedMonthlyPayment) + ' diff: ' + str(diffPaid) + ' Payment: '+ str(fixedMonthlyPayment)
            break
        if (diffPaid < 0):
            # min = fixedPayment
            print 'Payment: ' + str(fixedMonthlyPayment) + ' diff: ' + str(diffPaid) + ' Payment: '+ str(fixedMonthlyPayment)
            fixedMonthlyPayment = getPayment(fixedMonthlyPayment, monthlyPaymentUpperBound)
        #
        if (diffPaid > 0):
            # max = fixedPayment
            print 'Payment: ' + str(fixedMonthlyPayment) + ' diff: ' + str(diffPaid) + ' Payment: '+ str(fixedMonthlyPayment)
            fixedMonthlyPayment = getPayment(monthlyPaymentLowerBound, fixedMonthlyPayment)   
        
        # Next check with new fixed payment
        totalPaid = 0
        month = 1
        previousBalance = initialBalance
        continue 
        
    month += 1
    
print 'Lowest Payment: ' + str(fixedMonthlyPayment)