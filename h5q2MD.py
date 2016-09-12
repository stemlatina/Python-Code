# Marilu D

#User Input

userInt = int(input("Enter a positive integer: "))

#Setting Pattern
pat1 = '*'
pat2 = ' ' 

#For Loop First Pyramid
for lineNum in range(0,userInt+1):
    line = pat2*lineNum + pat1*((userInt - lineNum)*2+1)
    print(line)

#For Loop Second Pyramid/Reverse
for lineNum in range(userInt,0,-1):#-1 is step count
    line = pat2*lineNum + pat1*((userInt - lineNum)*2+1)
    print(line)

