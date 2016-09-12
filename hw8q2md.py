#Marilu D
#Program that has mutliple functions to remove an scramble phrases


#Part A Function
def func1 (phrase1):
    '''phrase and returns the first word in that phrase'''
    find = phrase1.find(" ")
    space = phrase1[:find]#Finds the spaces 
    return space



#Part B Function
def func2 (phrase2):
    '''removes the first word in that phrase'''
    find = phrase2.find(" ")
    space2 = phrase2[find+1:]#finds spaces
    return space2#returns word without first word


    
#Part C Function
def func3 (phrase3): 
    '''reverses the phrase'''
    countSpace = 0
    wordSpace = []
    for i in phrase3:
        if i == ' ':#if there is a space then +=1.
            countSpace += 1
        phrase4 = phrase3

    for i in range(countSpace):#for loop for the length of the spaces
        phrase4 = func2(phrase4)
        space = phrase4
        space2 = func1(space)
        wordSpace.append(space2)

    for i in range(2,countSpace + 1):#for loop for final output
        space +=  ' ' + wordSpace(-i) + ' '
    space +=  ' ' + func1(phrase3)
    return space
#returned the letter scrambled

            

#Part D Function
def main():
    userPhrase = input("Please enter a phrase: ")
    print (func1(userPhrase))
    print (func2(userPhrase))
    print (func3(userPhrase))
    
    
