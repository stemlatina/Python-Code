#Marilu D

#UserInput
inputNumber = int(input("Please enter a number here: "))

#For Loop
for i in range(1,inputNumber+1): #starting from 1 not 0 and include last...
    evenNumber = 0 #even def
    oddNumber = 0 #odddef
    digits = str(i) #i to str
    for n in digits: #If Statements
        if(int(n)%2 ==0): #including mod.
            evenNumber += 1 #end loop with even number
        else: #Else odd
            oddNumber += 1
#Print Results
    if evenNumber > oddNumber:
        print(i)
#end of program
