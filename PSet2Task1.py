balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 1
totalPaid = 0
while month <= 12:
    
    previousBalance = balance    
    monthlyInterestRate = annualInterestRate /12.0
    minimumMonthlyPaymentRate = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minimumMonthlyPaymentRate
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    balance = updatedBalance
    
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(minimumMonthlyPaymentRate, 2))
    print 'Remaining balance: ' + str(round(updatedBalance, 2) )
    if month == 12:
        print 'Total paid: ' + str(round(totalPaid))
        print 'Remaining balance: ' + str(round(updatedBalance, 2) )
        break
        
    month += 1