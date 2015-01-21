#
# Increse speed of computation fixed monthly payment by using bisectional search
#

balance = 3926 # comment beforesubmission
annualInterestRate = 0.2 # comment beforesubmission

monthlyInterestRate = annualInterestRate /12.0

month = 1
totalPaid = 0.0

initialBalance = balance #save initial balance
fixedMonthlyPayment = 10 #startig point
previousBalance = initialBalance
 
#check balance with fixed payment 
while month <= 12:

    totalPaid += fixedMonthlyPayment
    
    monthlyUnpaidBalance = previousBalance - fixedMonthlyPayment

    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    previousBalance = updatedBalance
        
    if month == 12 and updatedBalance > 0:
        fixedMonthlyPayment += 10
        totalPaid = 0
        month = 1
        previousBalance = initialBalance
        continue 
        
    month += 1
    
print 'Lowest Payment: ' + str(fixedMonthlyPayment)