# Program calculates the minimum fixed monthly payment needed in order pay off a credit card 
# balance within 12 months. By a fixed monthly payment, we mean a single number 
# which does not change each month, but instead is a constant amount that will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# The program should print out 
# one line: the lowest monthly payment that will pay off all debt in under 1 year, 
# for example: Lowest Payment: 180 

balance = 4773
annualInterestRate = 0.2
#monthlyPaymentRate = 0.04 - should be fixed!

monthlyInterestRate = annualInterestRate /12.0
month = 1
totalPaid = 0.0

updatedBalance = balance
fixedMonthlyPayment = 10 #startig point
while month <= 12:
    
    previousBalance = updatedBalance    
    #minimumMonthlyPaymentRate = monthlyPaymentRate * previousBalance
    totalPaid += fixedMonthlyPayment
    
    monthlyUnpaidBalance = previousBalance - fixedMonthlyPayment
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    #balance = updatedBalance
       
    
    
    if month == 12 and updatedBalance > 0:
        fixedMonthlyPayment += 10
        totalPaid = 0
        month = 1
        continue 
        
    month += 1
    
print 'Lowest Payment: ' + str(fixedMonthlyPayment)