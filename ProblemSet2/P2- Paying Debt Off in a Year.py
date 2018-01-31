# Write a program that calculates the minimum fixed monthly payment 
# needed in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, we mean a single number which does not 
# change each month, but instead is a constant amount that will be paid # each month.

def calcDebt(minPay, balance, annualInterestRate):
    for m in range(12):
        unpaidBal = balance - minPay
        interest = unpaidBal * (annualInterestRate/12.0)
        balance = unpaidBal + interest
    return balance
    
minPay = 10
while calcDebt(minPay, balance, annualInterestRate) > 0:
    minPay += 10
    
print("Lowest Payment: " + str(minPay))