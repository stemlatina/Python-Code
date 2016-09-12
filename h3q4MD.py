#Marilu D
#Q4MD

#User Input
side1 = float(input("Please enter the length of first side: "))
side2 = float(input("Please enter the length of second side: "))
side3 = float(input("Please enter the length of third side: "))

#If Statements
if side1 == side2 and side2 == side3 and side1 == side3:
    print("This is a equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is a isoseles triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3 and side1**2 + side2**2 == side3**2 or side1**2 + side2**2 == side3**2 or side1**2 + side2**2 == side3**2: 
    print("This is an isosceles right triangle.")
else:
    print("This is not an equilateral or isosceles triangle.")
    
