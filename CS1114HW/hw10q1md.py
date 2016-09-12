#Marilu D
#Q1

#importing
from random import randint

#problem 1A
def create_permutation(lst):
    '''returns a random permutation of items in lst'''
    ranList = []
    for item in lst:
        random(ranList,item)
    return ranList

def random(lst,item):
    '''function for random numbers for permutation'''
    countInd = 0
    for i in range(len(lst)):
        countInd = randint(0,len(lst)-1)
    lst.insert(countInd,item)
    
#problem 1B
def main():
    '''asks user for a positive integer, n, and prints a random permutation of the integer sequence 1,2, ..., n'''
    integer = int(input("Please enter an integer: ")) #asks users input
    lst = []
    for i in range(1,integer +1):
        lst.append(i)#adding back to the list a set of random nubmers
    print("Random permutation: " , create_permutation(lst))
main()
