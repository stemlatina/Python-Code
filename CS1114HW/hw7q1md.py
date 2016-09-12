#Marilu D


#User Input
rightShift = int(input("Enter a right shift: "))
capString = input("Enter a string with at least one capital letter: ")
cipherSpace = ''

#For Loop
for chr1 in capString:#if statement
    cipher = ord(chr1) + rightShift
    if cipher >= 91 and chr1.isupper():
        cipher -= 26
#elifs begins
    elif cipher >= 123 and chr1.islower():
        cipher -= 26

    elif ord(chr1) == 32 or ord(chr1) == 127:
        cipher = ord(chr1)

    elif (ord(chr1) in range(32,65)):
        cipher = ord(chr1)
    
    elif (ord(chr1) in range(91,97)):
        cipher = ord(chr1)

    elif (ord(chr1) in range(123,128)):
        cipher = ord(chr1)

    cipherSpace = cipherSpace + chr(cipher)
#print results
print(cipherSpace)


