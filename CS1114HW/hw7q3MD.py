#Marilu D

#Random guessing game

from random import randint
#guessing random range
guessNumRange = randint(1,100)

#define vars
chance = 1
rangeHigh = 100
rangeLow = 1
guessCont = True

#Print Statements
print("I thought of a number between 1 and 100! Try to guess it.")

#User Input
guess = int(input("Guess what the number is: "))

#while loop
while guessCont and guess != guessNumRange:
    #if statments
    if chance == 5:
        print("Out of guesses! My number is",guessNumRange)#number of guesses and chances to guess
    elif chance <= 4:
        if guess < guessNumRange:
            low = guess
            print("Wrong! Guess a number between",rangeLow,"to",rangeHigh,". You have",5-chance,"guesses left.")
        guess = int(input("Guess again: "))#userinput again
    chance += 1
if guess == guessNumRange: #if correct number
    print("Congratulations! You guessed correctly in",chance,"guesses.")
    guessCont = False #stop loop
        
