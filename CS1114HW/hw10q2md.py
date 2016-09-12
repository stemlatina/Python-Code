#Marilu D
#Q2

def add_list( lst1, lst2):
    '''returns a list consisting of the sum of the first numbers, the sum of the second numbers, etc.'''
    countIndex = 0 #def vars
    newList = []
    for item in lst1:#for loop for the index of the lists
        addItem = int(item) + int(lst2[countIndex])
        countIndex += 1
        newList.append(addItem)
    return newlist#return new lists

def main():
    lst1 = []#def vars
    lst2 = []
    numInput = int(input("Please enter a number for the first list: ")) #user input
    lst1.append(numInput)
    done = True
    doneAgain = False
    while done:#while loop for the users input if done/not done
        num2 = input("Please enter another number to add to the first list or type 'Done':")
        if num2.lower() == 'done':
            done = False
            numAgain = input("Enter anumber for the 2nd list: ")
            lst2.append(int(numAgain))
            doneAgain = True
        else:
            lst1.append(int(num2))
    while doneAgain:#while loop for the users input if done/not done
        num3 = input("Please enter another number to add ot the second list or type 'done': ")
        if num3.lower() == 'done':
            doneAgain = False

        else:
            lst2.append(int(num3))

        if len(lst1) != len(num3):
            print("The lists are diff. lengths")
        else:
            print(add_list(lst1,lst2))
#return
        main()
                
