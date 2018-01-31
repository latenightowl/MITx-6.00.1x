#Write a program that uses bounds and bisection search to find the
#smallest monthly payment to the cent such that we can pay off the debt 
#within a year.

def calcDebt(minPay, balance, annualInterestRate):
    for m in range(12):
        unpaidBal = balance - minPay
        interest = unpaidBal * (annualInterestRate/12.0)
        balance = unpaidBal + interest
    return balance

monthlyInterestRate = annualInterestRate/12.0
initLower = balance/12
initUpper = (balance*(1+monthlyInterestRate)**12)/12.0
minPay = (initLower + initUpper)/2
epsilon = 0.01

while abs(calcDebt(minPay, balance, annualInterestRate)) >= epsilon:
    if calcDebt(minPay, balance, annualInterestRate) > 0:
        initLower = minPay
    else:
        initUpper = minPay
    minPay = (initLower + initUpper)/2
    
print("Lowest Payment: " + str(round(minPay, 2)))
