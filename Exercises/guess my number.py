#Create a program that guesses a secret number!
#The user thinks of an integer between 0-100 and
#the computer makes guesses using bisection search.

low = 0
high = 100    

print("Please think of a number between 0 and 100!")
while 1 < 2:
    guess = int((low + high) / 2) 
    print("Is your secret number " + str(guess) + "?")
    judg = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if judg == 'h':
        high = guess
    elif judg == 'l':
        low = guess
    elif judg == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
    "guess - (high + low) / 2"
print("Game over. Your secret number was: " + str(guess))
