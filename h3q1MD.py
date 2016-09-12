#Marilu D
#Program A

#User Input
userNum1 = float(input("Please enter weight in kilograms: "))
userNum2 = float(input("Please enter height in meters: "))

#math
BMI = userNum1/userNum2**2


#Results
print("BMI is: ",BMI,)


#Program B
userNum3 = int(input("Please enter weight in pounds: "))
userNum4 = int(input("Please enter height in inches: "))


#math
num3Metric = userNum3 * 0.453592
num4Metric = userNum4 * 0.0254
BMI2 = num3Metric/num4Metric**2


#Results
print("BMI is: ",BMI2,)

#If Statements

if (BMI2 < 18.5):
    print("You are Underweight")
elif (BMI2 >= 18.5 < 24.9):
    print("You are Normal Weight")
elif (BMI2 > 25.0 <= 29.9):
    print("You are Over Weight")
elif (BMI2 > 30.0):
    print("You are Obese")

