#Marilu D
#Q3


def create_prefix_lists(lst):
    '''return a sequence of lists, each containing a prefix of lst'''
    len1 = int(len(lst)) #find length of lost
    newList1 = []#space for new list
    for i in range(len1+1):
        newList2 = []
        for m in range(i):#add to new list
            newList2.append(lst[m])
            newList1.append(newList2)
        return newList1

def main():#calling all the functions together
    newList2 = []
    userInput = input("Please enter a value to add to the list: ")#user input
    newList2.append(userInput)
    adding = True
    while adding:#while loop to see if done
        userInput = input("Please add another value or type 'Done':")
        if userInput.lower() == 'done':
            adding = False
        else:#printing new list
            newList2.append(userInput)
    print(create_prefix_lists(newList2))
          
main()

    
