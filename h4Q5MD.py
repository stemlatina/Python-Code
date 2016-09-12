# Marilu D

#User Input
pass1 = input("Enter your password: ")

#counters

uppercaseCounter = 0
lowercaseCounter = 0
digit2Counter = 0
specialCounter = 0

#For Loop
for letter in pass1:
    if letter.isupper():
        uppercaseCounter += 1
    elif letter.islower():
        lowercaseCounter += 1
    elif letter.isdigit():
        digit2Counter += 1
    elif letter == '!' or letter == '@' or letter == '#' or letter == '$':
        specialCounter += 1
if uppercaseCounter >= 2 and lowercaseCounter >= 1 and digit2Counter >=2 and specialCounter >= 1:
    print(pass1,"is a valid Password")
else:
    print(pass1,"is not a valid password.")
#Results

