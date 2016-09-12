#homework 3 question 4

a = float(input("Length of first side: "))
b = float(input("Length of second side: "))
c = float(input("Length of third side: "))

if a == b and b == c and a ==c :
    print("This is a equilateral triangle")
elif a == b or a == c or b == c:
    print("this is a isoseles triangle")
elif a == b or a == c or b == c and a**2 + b**2 == c**2: 
    print("this is an isosceles right triangle ")
else:
    print("neither")
    
