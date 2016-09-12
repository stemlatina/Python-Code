#Marilu D
#Q5MD

#User Input
a = float(input("Please enter the length of first side: "))
b = float(input("Please enter the length of second side: "))
c = float(input("Please enter the length of third side: "))

#If Statements
if a == b and b == c and a ==c :
    print("This is a equilateral triangle")
elif a == b or a == c or b == c:
    print("This is a isoseles triangle.")
elif a == b or a == c or b == c and a**2 + b**2 == c**2 or a**2 + b**2 == c**2 or a**2 + b**2 == c**2: 
    print("This is an isosceles right triangle.")
else:
    print("This is not an equilateral or isosceles triangle.")
 
