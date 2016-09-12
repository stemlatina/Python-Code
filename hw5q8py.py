#Marilu D

#User Input
int1 = int(input("Please enter a postitive integer: "))
#def space
space = ' '

#For Loop
for i in range(1,int1+1):
    space2 = ''
    for f in range(1,i+1): #for loop in for loop
        space2 += str(f)
    print(space*int1 + space2)
    int1 -= 1 #end loop
    #results
