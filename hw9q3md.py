#Marilu D
#Q3

#Encoder Function
lst1 = [1, 2, 3, 4, 5, 6]
def reverse1(lst):
    '''reverses the list'''
    newList = []
    for i in range(len(lst)):#turning into index form to append
        newList.append(lst[len(lst) - i -1])
    return newList
        

def reverse2(lst):
    '''reverse a string/list'''
    lst.reverse()
    
    

def main():#call the functions
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse1(lst1)
    print("After reverse1, lst1 is ", lst1, " and the returned list is ", rev_lst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    reverse2(lst2)
    print("After reverse2, lst2 is", lst2)
