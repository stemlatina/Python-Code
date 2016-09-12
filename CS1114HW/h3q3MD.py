#Marilu D
#Q3MD

#import
import math

#User Input
a = float(input("Please enter a value for A: "))
b = float(input("Please enter a value for B: "))
c = float(input("Please enter a value for C: "))

#Math
num1 = ((b**2)-(4*a*c))

#If Statement
if (a==0 and b==0 and c==0):
    print("There are infinite solutions")
#Elif Statements
elif (a==0 and b==0):
    print("There is no solution")
    
elif (num1 == 0):
    ans = -b/(2*a)
    print("The only real solution is x=", ans)
elif (num1 < 0):
    print("There are no real solutions")
elif (num1 > 0):
    ans1 = (-b - math.sqrt(num1))/2*a
    ans2 = (-b + math.sqrt(num1))/2*a
    print("There are multiple solutions, x= ", ans1,ans2)
#Results
