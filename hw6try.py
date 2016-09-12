import random

#Problem 3
#UserInput
print ("I thought of a number between 1 and 100! Try to guess it.")
guess = 0

#Importing
num1 = random.randint(1,100)

#def vars
chances = 1
rangeHigh = 100
rangeLow = 1
correct = False

#while loop
while chances != 6 and guess != num1:
	print("Range:", rangeLow, rangeHigh ,"Number of guesses left:", (6 - chances))
	guess = int(input("Your Guess:"))
	if chances <= 6:
		if guess < num1:
			if rangeLow < guess: 
				rangeLow = guess + 1
			print("Wrong! my number is bigger, try again.")
		elif guess > num1:
			if rangeHigh > guess:
				rangeHigh = guess - 1
			print("Wrong! my number is smaller, try again.")
		else: # guess is correct!
			print("Your Guess is correct. You guessed", chances, "times")
			correct = True
		chances += 1

if correct == False:
	print("Sorry, you used all guesses, good luck next time!")
