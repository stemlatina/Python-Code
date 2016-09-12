#Marilu D

def print_shifted_triangle(n,m,symbol):
    '''This function prints the first shifted angle'''
    for size in range(n):#For loop for the and depth of the trianles.
        print(" " * (m-n) + " " * (n-size) + symbol * (2*size+1))

def print_pine_tree(n,m,symbol):
    '''Prints the rest of the tree'''
    for size2 in range(n):#For loop for the shape sie and symbol of the triangle
        print_shifted_triangle(size2 + 2, m, symbol)

def main():#Calling the functions
    print_pine_tree(4, 8, "#")

main()


#call main
