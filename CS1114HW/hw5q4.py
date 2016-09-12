#Marilu D

#User Input
num1 = int(input("Please enter a positive integer: "))

#def var
romSpace = ' '

#While Loop
while num1 > 0:#Ifstatements for ever roman numeral option
    if num1 > 1000 or num1 == 1000:
        num1 -= 1000
        romSpace += 'M'
    elif num1 > 500 or num1 == 500: #elif statments for every option ever
        num -= 500
        romSpace += 'D'
    elif num1 > 100 or num1 == 100:
        num1 -= 100
        romSpace += 'C'
    elif num1 > 50 or num1 == 50:
        num1 -= 50
        romSpace += 'L'
    elif num1 > 10 or num1 == 10:
        num1 -= 10
        romSpace += 'X'
    elif num1 > 5 or num1 == 5:
        num1 -= 5
        romSpace += 'V'
    elif num1 > 1 or num1 == 1:
        num1 -= 1
        romSpace += 'I'

print(romSpace)
#Results
#program end
