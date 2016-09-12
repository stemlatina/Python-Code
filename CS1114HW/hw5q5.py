#Marilu D

#A
#User Input
lengthSeq = int(input("Please enter the length of the sequence: "))

#Define Var.
total = 1

#For Loop
print("Please enter your sequence: ")
for i in range (0,lengthSeq):
    int1 = int(input())
    total = total *int1
    #Math
print("The geometric mean is:",total**(1/lengthSeq))


#B
#User Input

#define vars.
continueLoop = True
total = 1
count = 0
#While loop
print("Please enter a positive integer or 'DONE' when finished adding numbers: ")
while continueLoop:
    int2 = input()
    if int2 == 'DONE'or int2 == 'done': #If
        continueLoop = False
    else: #else
        count += 1
        total = total*int(int2)
print("The geometric mean is:",total**(1/count)) #results
