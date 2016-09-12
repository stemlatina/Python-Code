#Marilu 
#Q1

lst = [-19, -3, 30, -1, 0, -25]
def max_abs_val(lst):
    '''returns the maximum absolute value in lst.'''

    for i in range(len(lst)):#lst to index
        if lst[i] < 0:
            lst[i] = abs(lst[i])#doing the absolute value

    current_max = 0
    for j in lst:
        if j > current_max:#printing the max value
            current_max = j

    return current_max

def main():#calling functions
    res = max_abs_val(lst)
    print(res)

main()
    
