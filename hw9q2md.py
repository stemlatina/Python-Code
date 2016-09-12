#Marilu D
#Q2

lst = ['a', 'b', 10, 'bb', 'a']
val = 'a'
def find_all (lst,val):
    '''returns a list containing indices of the occurrences of val in lst.'''
    newList = []
    for i in range(len(lst)):#making it countable in index form
        if lst[i] == val:
            newList.append(i)#adding to the new list

    return newList
