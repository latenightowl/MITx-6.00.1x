# Write a program to calculate the credit card balance after one year 
# if a person only pays the minimum monthly payment required by the  
# credit card company each month.
# 
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

for m in range(12):
    minPay = balance*monthlyPaymentRate
    unpaidBal = balance - minPay
    interest = unpaidBal * (annualInterestRate/12.0)
    balance = unpaidBal + interest

print("Remaining balance: " + str(round(balance, 2)))